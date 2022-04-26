from django.db import models
from blog.models import Category
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from .utilities.models_validatior import validate_video_extension
from common.tools import convert_english_number_to_persian_number
from django.utils.timezone import now
from django.db.models import UniqueConstraint, Q
import mutagen
from math import ceil

from django.contrib.auth import get_user_model
User = get_user_model()

class Course(models.Model):
    title = models.CharField(max_length=1024)
    detail = RichTextField()
    is_promote = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT)
    desribe_video = models.FileField(upload_to="course/video", validators=[validate_video_extension], null=True, blank=True)
    amount = models.PositiveBigIntegerField(default=0)
    buy_counter = models.PositiveIntegerField(default=0, editable=False)
    off = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ]
    )
    image = models.ImageField(upload_to="course/image")
    date = models.DateTimeField(auto_now=True)
    is_expire = models.BooleanField(default=False)
    supported_course = models.ManyToManyField('self', blank=True)

    @classmethod
    def get_most_off(cls):
        return cls.objects.select_related('category', 'teacher').filter(is_promote=True).order_by('-off')

    @classmethod
    def get_most_sales(cls):
        return cls.objects.all().prefetch_related('teacher', 'category').order_by('-buy_counter' , '?')[0:4]

    @classmethod
    def get_newest_course(cls):
        return cls.objects.all().prefetch_related('teacher', 'category').order_by('-date' , '?')[0:4]

    def get_course_duration(self):
        contents = Content.objects.filter(season__course__id=self.id)
        length = 0
        for content in contents :
            video_info = mutagen.File(content.video).info
            length += int(video_info.length)
        return convert_english_number_to_persian_number (ceil(length / 60))
    
    def is_in_user_card(self, request):
        return Course.objects.filter(id=self.id , card__user=request.user).filter(Q(card__status=Card.INPROCESS) | Q(card__status=Card.FREEZE)).exists()

    def is_in_user_paid_card(self, request):
        return Course.objects.filter(id=self.id ,card__status=Card.PAID, card__user=request.user).exists()

    def content_counter(self):
        counter = sum( season.content_set.count() for season in self.season_set.all() )
        return convert_english_number_to_persian_number(counter)

    def season_counter(self):
        return convert_english_number_to_persian_number(self.season_set.count())

    def list_of_supported_course(self):
        return self.supported_course.exclude(id=self.id).filter(is_expire=False)

    def teacher_name(self):
        return self.teacher.full_name()

    def get_amount_without_off(self):
        return self.amount
    
    def persian_amount_without_off(self):
        return convert_english_number_to_persian_number(self.get_amount_without_off())

    def persian_off(self):
        return convert_english_number_to_persian_number(self.off)

    def get_amount(self):
        return int(self.amount - ( (self.off / 100) * self.amount ))

    def get_raw_amount(self):
        raw_amount = self.get_amount()
        return convert_english_number_to_persian_number(raw_amount)

    def persian_amount(self):
        return convert_english_number_to_persian_number(self.amount)
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.id}, counter: {self.buy_counter})"

class Season(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    detail = RichTextField()

    def get_contents(self):
        return self.content_set.all()

    def content_counter(self):
        return convert_english_number_to_persian_number(self.content_set.count())
    
    @classmethod
    def get_payed_course(cls, request):
        return cls.objects.filter(course__card__status=Card.PAID, course__card__user=request.user)

class Content(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    main_image = models.ImageField(upload_to="content/image", null=True, blank=True)
    title = models.CharField(max_length=1024)
    detail = RichTextField(null=True, blank=True)
    video = models.FileField(upload_to="content/video", validators=[validate_video_extension], null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def get_content_size(self):
        print(self.video)
        video_info = mutagen.File(self.video)
        print(dir(video_info))
        return 10000

class Card(models.Model):
    FREEZE = 'FR'
    PAID = 'PD'
    INPROCESS = 'IP'
    CARD_STATUS = [
        (FREEZE, 'FREEZE'),
        (PAID, 'PAID'),
        (INPROCESS, 'INPROCESS'),
    ]
    is_counter_added_to_courses = models.BooleanField(default=False, editable=False)
    courses = models.ManyToManyField(Course, blank=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    time_created = models.DateTimeField(default=now)
    time_change_status = models.DateTimeField(default=now)
    status = models.CharField(
        max_length=2,
        choices=CARD_STATUS,
        default=INPROCESS,
    )

    class Meta :
        constraints = [
            UniqueConstraint(
                fields=[
                    'user',
                ],
                condition=Q(status='IP') | Q(status='FR'),
                name='unique_active_card',
            ),
        ]

    def __str__(self):
        return f"{self.__class__.__name__}({self.id} , {self.user.username}, {self.status})"
    
    @classmethod
    def current_card(cls, request):
        queryset = cls.objects.exclude(status=cls.PAID).prefetch_related('courses')
        card, is_created = queryset.get_or_create(user=request.user)
        return card, is_created
    
    def add_course(self, course):
        self.courses.add(course)
    
    def delete_course(self, course):
        self.courses.remove(course)
    
    def courses_count(self):
        return self.courses.count()
    
    def calculate_amount_without_off(self):
        return sum( course.get_amount_without_off() for course in self.courses.all() )

    def calculate_amount(self):
        return sum( course.get_amount() for course in self.courses.all() )
    
    def persian_amount_without_off(self):
        return convert_english_number_to_persian_number(self.calculate_amount_without_off())

    def persian_amount(self):
        return convert_english_number_to_persian_number(self.calculate_amount())
    
    def change_status(self, status):
        self.status = status
        self.time_change_status = now()
        self.save()

        

from django.db import models
from blog.models import Category
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from .utilities.models_validatior import validate_video_extension
from common.tools import convert_english_number_to_persian_number

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

    def persian_off(self):
        return convert_english_number_to_persian_number(self.off)

    def get_raw_amount(self):
        raw_amount = int(self.amount - ( (self.off / 100) * self.amount ))
        return convert_english_number_to_persian_number(raw_amount)

    def persian_amount(self):
        return convert_english_number_to_persian_number(self.amount)

class Season(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    detail = RichTextField()

class Content(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to="content/image", null=True, blank=True)
    title = models.CharField(max_length=1024)
    detail = RichTextField(null=True, blank=True)
    video = models.FileField(upload_to="content/video", validators=[validate_video_extension], null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

class Card(models.Model):
    FREEZE = 'FR'
    PAID = 'PD'
    INPROCESS = 'IP'
    CARD_STATUS = [
        (FREEZE, 'FREEZE'),
        (PAID, 'PAID'),
        (INPROCESS, 'INPROCESS'),
    ]
    courses = models.ManyToManyField(Course, blank=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=CARD_STATUS,
        default=INPROCESS,
    )

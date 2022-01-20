from statistics import mode
from django.db import models
from blog.models import Category
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from utilities.models_validatior import validate_video_extension

class Course(models.Model):
    title = models.CharField(max_length=1024)
    detail = RichTextField()
    category = models.ForeignKey(Category)
    teacher = models.ForeignKey(User)
    off = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ]
    )
    image = models.ImageField(upload_to="course/image")
    date = models.DateTimeField(auto_now=True, auto_now_add=True)

class Content(models.Model):
    course = models.ForeignKey(Course)
    main_image = models.ImageField(upload_to="content/image")
    title = models.CharField(max_length=1024)
    detail = RichTextField()
    video = models.FileField(upload_to="course/video", validators=[validate_video_extension])
    date = models.DateTimeField(auto_now=True, auto_now_add=True)

class Commnet(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    user = models.ForeignKey(User, null=True)
    text = models.CharField(max_length=1024)
    course = models.ForeignKey(Course)
    parent = models.ForeignKey('self' , related_name='parent_comment')
    child = models.ForeignKey('self' , related_name='child_comment')
    date = models.DateTimeField(auto_now=True, auto_now_add=True)


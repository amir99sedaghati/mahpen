from django.db import models
from ckeditor.fields import RichTextField
from course.utilities.models_validatior import validate_video_extension
from colorfield.fields import ColorField

from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="category/image")
    is_promote = models.BooleanField(default=False)
    date_publish = models.DateField(auto_now=True)
    color = ColorField(default="#88153e")
    title_color = ColorField(default="#3d8835")
    text_color = ColorField(default="#ffffff")
    text = RichTextField()

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.title})'

class PostAbstract(models.Model):
    auhtor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    text = RichTextField()
    image = models.ImageField(upload_to="post/image")
    is_promote = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_publish = models.DateTimeField(auto_now=True)

    @classmethod
    def get_promoted_post(cls):
        return cls.objects.all().filter(is_promote=True)[0:8]

    @classmethod
    def get_related_object(cls, object):
        return cls.objects.exclude(id=object.id).filter(category__id=object.category.id)[0:4]

    class Meta :
        abstract = True
    
    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.title})'

class Post(PostAbstract):
    pass

class Video(PostAbstract):
    video = models.FileField(upload_to="content/video", validators=[validate_video_extension], null=True, blank=True)


from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="category/image")
    is_promote = models.BooleanField(default=False)

class Post(models.Model):
    title = RichTextField(max_length=1024)
    text = RichTextField()
    image = models.ImageField(upload_to="post/image")
    is_promote = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

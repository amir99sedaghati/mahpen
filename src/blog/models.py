from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="category/image")
    is_promote = models.BooleanField(default=False)
    date_publish = models.DateField(auto_now=True)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.title})'

class Post(models.Model):
    title = RichTextField(max_length=1024)
    text = RichTextField()
    image = models.ImageField(upload_to="post/image")
    is_promote = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_publish = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.title})'

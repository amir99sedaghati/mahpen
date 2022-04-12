from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_profile = models.ImageField(upload_to='user/profile', blank=True)

    def full_name(self) :
        return f"{self.first_name} {self.last_name}"

User._meta.get_field('first_name').blank = False
User._meta.get_field('last_name').blank = False 
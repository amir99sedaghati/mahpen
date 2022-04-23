from django.db import models
from django.contrib.auth.models import AbstractUser
from common.tools import convert_english_number_to_persian_number

class User(AbstractUser):
    user_profile = models.ImageField(upload_to='user/profile', blank=True)
    wallet = models.PositiveBigIntegerField(default=0, editable=False)

    def full_name(self) :
        return f"{self.first_name} {self.last_name}"
    
    def get_persian_wallet_value(self):
        return convert_english_number_to_persian_number(self.wallet)

User._meta.get_field('first_name').blank = False
User._meta.get_field('last_name').blank = False 
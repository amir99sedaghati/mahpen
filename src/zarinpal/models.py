from django.db import models
from course.models import Card

class Pay(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    status = models.PositiveIntegerField()
    authority = models.TextField()
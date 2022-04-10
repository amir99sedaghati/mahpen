from django.db import models
from course.models import Card
from django.utils.timezone import now

class Pay(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    email = models.EmailField(blank=True, null=True)
    status = models.PositiveIntegerField()
    authority = models.TextField(blank=True, null=True)
    time_tr = models.DateTimeField(default=now)
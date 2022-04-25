from .models import *
from django.db.models import F
from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver

@receiver(post_save, sender=Card)
def edit_is_video_filed_in_instance_before_save(sender, instance, **kwargs):
    if instance.status == Card.PAID and not instance.is_counter_added_to_courses :
        instance.courses.all().update(buy_counter=F('buy_counter') + 1)
        instance.is_counter_added_to_courses = True
        instance.save()

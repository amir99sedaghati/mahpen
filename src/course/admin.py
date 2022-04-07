from statistics import mode
from django.contrib import admin
from . import models

admin.site.register(models.Course)
admin.site.register(models.Card)
admin.site.register(models.Content)
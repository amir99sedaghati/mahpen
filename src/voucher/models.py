from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import NoSpaceValidator

class Voucher(models.Model):
    off = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ]
    )
    name = models.CharField(max_length=256, validators=[NoSpaceValidator], unique=True)
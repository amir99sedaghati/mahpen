from django.contrib import admin
from .models import Pay, WalletTransaction

admin.site.register(Pay)
admin.site.register(WalletTransaction)
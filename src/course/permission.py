from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from .models import Card

class ShouldNotHaveEnableCard(PermissionRequiredMixin): 
    def has_permission(self):
        card = Card.objects.filter(status=Card.FREEZE, user=self.request.user)
        if card.exists() :
            messages.warning(self.request , self.permission_message)
        return not card.exists()
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from .models import Card
from django.utils.timezone import now
from datetime import timedelta 

class ShouldNotHaveEnableCard(PermissionRequiredMixin): 
    return_to_inprocess = 'شما یک سبد خرید داشتید که با موفقیت پرداخت نشد، آنرا به وضعیت پرداخت نشده بازگرداندیم .'
    
    def has_permission(self):
        card, is_created = Card.current_card(request=self.request)
        if (not is_created) and (card.status == Card.FREEZE) :
            delta_time = card.time_change_status + timedelta(minutes=15)
            if delta_time <  now():
                card.change_status(status=Card.INPROCESS)
                messages.warning(self.request , self.return_to_inprocess)
                return True
            messages.warning(self.request , self.card_status_messgage)
            return False
        return True
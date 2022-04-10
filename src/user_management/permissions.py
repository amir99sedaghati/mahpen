from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages

class IsAnnonymous(UserPassesTestMixin): 
    def test_func(self):
        is_anonymous = self.request.user.is_anonymous
        if not is_anonymous :
            messages.warning(self.request , self.permission_message)
        return is_anonymous

class IsAuthenticated(UserPassesTestMixin): 
    def test_func(self):
        is_authenticated = self.request.user.is_authenticated
        if not is_authenticated :
            messages.warning(self.request , self.permission_message)
        return is_authenticated
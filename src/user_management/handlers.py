from django.views.generic.base import TemplateView

class Handler(TemplateView):
    template_name = 'user_management/handler.html'
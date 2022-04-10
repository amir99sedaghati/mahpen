from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        from course.models import Course
        from .models import Category
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.order_by('-date').filter(is_promote=True)[0:3]
        context['offers'] = Course.objects.select_related('category', 'teacher').filter(is_promote=True).order_by('off')[0:4]
        context['promoted_categotories'] = Category.objects.filter(is_promote=True)
        context['categotories'] = Category.objects.all()
        return context


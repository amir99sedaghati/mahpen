from django.views.generic import TemplateView
from course.views import CardView
from . import filtering
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Video
from course import filtering as course_filtering

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
        if self.request.user.is_authenticated :
            context['card'] = CardView(request=self.request).get_object()
        return context


class PostListView(ListView):
    template_name = 'post/post_list.html'
    paginate_by = 16

    def get_queryset(self):
        qs = filtering.PostFiltering(data=self.request.GET, queryset=Post.objects.all().order_by('-id')).filter()
        return course_filtering.ordering(qs, self.request)
    
    def get_context_data(self, **kwargs):
        from blog.models import Category
        context = super().get_context_data(**kwargs)
        context['promote_posts'] = Post.get_promoted_post()
        context['categotories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_post'] = Post.get_related_object(object=context['post'])
        return context

class VideoDetailView(DetailView):
    model = Video
    template_name = 'video/video_detail.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_videos'] = Video.get_related_object(object=context['video'])
        return context

class VideoListView(ListView):
    template_name = 'video/video_list.html'
    paginate_by = 16

    def get_queryset(self):
        qs = filtering.VideoFiltering(data=self.request.GET, queryset=Video.objects.all().order_by('-id')).filter()
        return course_filtering.ordering(qs, self.request)
    
    def get_context_data(self, **kwargs):
        from blog.models import Category
        context = super().get_context_data(**kwargs)
        context['promote_posts'] = Video.get_promoted_post()
        context['categotories'] = Category.objects.all()
        return context
from . import views
from django.urls import path

urlpatterns = [
    path('card/', views.CardView.as_view(), name='card-detail'),
    path('card/addcourse/<int:pk>/', views.AddCourseToCardView.as_view(), name='add-course-to-card'),
    path('card/delcourse/<int:pk>/', views.DeleteCourseFromCardView.as_view(), name='del-course-from-card'),
    path('courses/', views.CoursesView.as_view(), name='course-list'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
]


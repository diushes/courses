from django.urls import path, include
from .views import CourseListView, SingleCourseView

app_name = "courses"
urlpatterns = [
    path('', CourseListView.as_view(), name='courses'),
    path('<int:pk>/', SingleCourseView.as_view(), name='retrieve'),
]

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import CourseSerializer
from .models import Course

class CourseListView(ListCreateAPIView):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleCourseView(RetrieveDestroyAPIView):
    model = Course
    serializer_class = CourseSerializer
    queryset = Course.objects.all()



from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from online_learning.models import Course, Lesson
from online_learning.serialiser import CourseSerialiser, LessonSerialiser


class CourseSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerialiser


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser


class LessonUdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser

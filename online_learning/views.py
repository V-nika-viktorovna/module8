from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from online_learning.models import Course, Lesson
from online_learning.serialiser import (CourseDetailseSerialiser,
                                        CourseSerialiser, LessonSerialiser,
                                        PaymentsSerialiser)
from users.models import Payments


class CourseSet(ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailseSerialiser
        return CourseSerialiser


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


class PaymentsVievSet(ModelViewSet):
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ('data_pay',)
    filterset_fields = ('course_pay', 'lesson_pay',)
    search_fields = ('payment_method',)
    serializer_class = PaymentsSerialiser

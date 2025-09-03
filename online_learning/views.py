from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from online_learning.models import Course, Lesson, Payments, Subscription
from online_learning.pagination import OnlineLearningPagination
from online_learning.serialiser import (CourseDetailseSerialiser,
                                        CourseSerialiser, LessonSerialiser,
                                        PaymentsSerialiser)
from users.permissions import Moder, Owner


class CourseSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = OnlineLearningPagination

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailseSerialiser
        return CourseSerialiser

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~Moder,)

        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (Moder | Owner,)

        if self.action == 'destroy':
            self.permission_classes = (Owner | ~Moder,)

        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.groups.filter(name="moders").exists():
            return super().get_queryset()
        else:
            return super().get_queryset().filter(owner=self.request.user)


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser
    permission_classes = [IsAuthenticated, ~Moder]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser
    pagination_class = OnlineLearningPagination

    def get_queryset(self):
        if self.request.user.groups.filter(name="moders").exists():
            return super().get_queryset()
        else:
            return super().get_queryset().filter(owner=self.request.user)


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser
    permission_classes = [IsAuthenticated, Owner | Moder]


class LessonUdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser
    permission_classes = [IsAuthenticated, Owner | Moder]


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerialiser
    permission_classes = [IsAuthenticated, Owner]


class PaymentsVievSet(ModelViewSet):
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ('data_pay',)
    filterset_fields = ('course_pay', 'lesson_pay',)
    search_fields = ('payment_method',)
    serializer_class = PaymentsSerialiser


class SubscriptionAPIView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "подписка добавлена"
        return Response({"message": message})

from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import AllowAny

from users.models import User
from users.serialiser import UserSerialiser


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class LessonListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class LessonUdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payments
from users.serialiser import PaymentsSerialiser


class PaymentsVievSet(ModelViewSet):
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ('data_pay',)
    filterset_fields = ('course_pay', 'lesson_pay',)
    search_fields = ('payment_method',)
    serializer_class = PaymentsSerialiser

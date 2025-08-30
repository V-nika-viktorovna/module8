from rest_framework.serializers import ModelSerializer

from users.models import Payments


class PaymentsSerialiser(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"

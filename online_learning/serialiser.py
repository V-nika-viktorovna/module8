from rest_framework.serializers import (CharField, ModelSerializer,
                                        SerializerMethodField)

from online_learning.models import Course, Lesson, Payments, Subscription
from online_learning.validators import link_validator


class LessonSerialiser(ModelSerializer):
    title = CharField(validators=[link_validator])
    description = CharField(validators=[link_validator])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerialiser(ModelSerializer):
    title = CharField(validators=[link_validator])
    description = CharField(validators=[link_validator])

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailseSerialiser(ModelSerializer):

    count_lessons_course = SerializerMethodField()
    lessons_course = LessonSerialiser(read_only=True, many=True)
    subscription = SerializerMethodField(read_only=True)

    def get_count_lessons_course(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        return Subscription.objects.filter(course=course, user=self.context["request"].user).exists()

    class Meta:
        model = Course
        fields = ("title",  "preview", "description", "count_lessons_course", "lessons_course", "subscription")


class PaymentsSerialiser(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

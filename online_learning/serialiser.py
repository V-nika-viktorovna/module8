from rest_framework.serializers import ModelSerializer
from online_learning.models import Course, Lesson


class CourseSerialiser(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerialiser(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

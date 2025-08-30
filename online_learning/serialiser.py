from rest_framework.serializers import ModelSerializer, SerializerMethodField

from online_learning.models import Course, Lesson
from users.models import Payments


class LessonSerialiser(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerialiser(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailseSerialiser(ModelSerializer):

    count_lessons_course = SerializerMethodField()
    lessons_course = LessonSerialiser

    def get_count_lessons_course(self, lesson):
        return Lesson.objects.filter(lesson=lesson.course).count()

    class Meta:
        model = Course
        fields = ("title",  "preview", "description", "count_lessons_course", "lessons_course")


class PaymentsSerialiser(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"

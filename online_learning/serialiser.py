from rest_framework.serializers import ModelSerializer, SerializerMethodField

from online_learning.models import Course, Lesson, Payments


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
    lessons_course = LessonSerialiser(read_only=True, many=True)

    def get_count_lessons_course(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("title",  "preview", "description", "count_lessons_course", "lessons_course")


class PaymentsSerialiser(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"

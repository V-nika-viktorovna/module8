from django.urls import path
from rest_framework.routers import SimpleRouter

from online_learning.views import (CourseSet, LessonCreateApiView, LessonListApiView,
                                   LessonRetrieveApiView, LessonUdateApiView, LessonDestroyApiView)
from online_learning.apps import OnlineLearningConfig

app_name = OnlineLearningConfig.name

router = SimpleRouter()
router.register("", CourseSet)

urlpatterns = [
                path("lesson/create/", LessonCreateApiView.as_view(), name="lesson_create"),
                path("lesson/", LessonListApiView.as_view(), name="lesson_list"),
                path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrive"),
                path("lesson/<int:pk/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"),
                path("lesson/<int:pk>/update/", LessonUdateApiView.as_view(), name="lesson_update"),
              ] + router.urls

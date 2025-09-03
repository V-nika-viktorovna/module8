from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from online_learning.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test4@mail.ru")
        self.course = Course.objects.create(title="Test", description="Test")
        self.lesson = Lesson.objects.create(title="Test1", description="Test1", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("online_learning:lesson_retrive", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)
        self.assertEqual(data.get("course"), self.lesson.course.pk)

    def test_lesson_create(self):
        url = reverse("online_learning:lesson_create")
        data = {
            "title": "Test_lesson",
            "description": "Test_lesson",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("online_learning:lesson_update", args=(self.lesson.pk,))
        data = {"title": "Updated_Test", "description": "Test"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.get(pk=self.lesson.pk).title, "Updated_Test")

    def test_lesson_delete(self):
        url = reverse("online_learning:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("online_learning:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test4@mail.ru")
        self.course = Course.objects.create(title="Ttst course", description="test course")
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse("online_learning:subscription")
        data = {"user": self.user.pk, "course": self.course.pk}
        response = self.client.post(url, data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "подписка добавлена")
        self.assertEqual(Subscription.objects.all().count(), 1)

    def test_subscribe_delete(self):
        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        url = reverse("online_learning:subscription")
        response = self.client.post(url, data=data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "подписка удалена")
        self.assertEqual(Subscription.objects.all().count(), 0)

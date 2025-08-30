from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса', help_text='Название курса')
    preview = models.ImageField(null=True, blank=True, upload_to='online_learning/photo')
    description = models.TextField(null=True, blank=True, verbose_name='описание')

    class Mete:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название урока', help_text='Название урока')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,
                               verbose_name='Название урока', help_text='Название урока', null=True, blank=True)
    preview = models.ImageField(null=True, blank=True, upload_to='online_learning/photo', verbose_name='Фото')
    description = models.TextField(null=True, blank=True, verbose_name='описание')

    class Mete:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f'{self.title} курс: {self.course}'

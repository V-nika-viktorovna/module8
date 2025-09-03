from django.db import models

from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса', help_text='Название курса')
    preview = models.ImageField(null=True, blank=True, upload_to='online_learning/photo')
    description = models.TextField(null=True, blank=True, verbose_name='описание')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Владелец курса', help_text='Владелец курса')

    class Mete:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название урока', help_text='Название урока')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,
                               verbose_name='Название курса', help_text='Название курса', null=True, blank=True)
    preview = models.ImageField(null=True, blank=True, upload_to='online_learning/photo', verbose_name='Фото')
    description = models.TextField(null=True, blank=True, verbose_name='описание')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Владелец урока', help_text='Владелец урока')

    class Mete:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f'{self.title} курс: {self.course}'


class Payments(models.Model):
    choice_payment_method = [
        ("cash", "наличные"),
        ("payment by card", "оплата картой"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Имя пользователя', help_text='Имя пользователя')
    data_pay = models.DateField(verbose_name='Дата оплаты', help_text='Дата оплаты', null=True, blank=True)
    course_pay = models.ForeignKey(Course, on_delete=models.SET_NULL,
                                   verbose_name='Оплаченный курс', help_text='Оплаченный курс', null=True, blank=True)
    lesson_pay = models.ForeignKey(Lesson, on_delete=models.SET_NULL,
                                   verbose_name='Оплаченный урок', help_text='Оплаченный урок', null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=choice_payment_method, default='payment by card',
                                      verbose_name='Способ оплаты', help_text='Способ оплаты', null=True, blank=True)
    session_id = models.CharField(max_length=255, verbose_name="ID сессии",
                                  help_text='Укажите ID Сессии', null=True, blank=True)
    payment_link = models.URLField(max_length=400, verbose_name="Ссылка на оплату",
                                   help_text='Укажите ссылку на оплату', null=True, blank=True)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        if self.lesson_pay:
            return f'оплата за {self.lesson_pay}'
        elif self.course_pay:
            return f'оплата за {self.course_pay}'
        else:
            return f'оплата в размере {self.payment_amount}'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Подписчик', help_text='Подписчик'
                             )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", help_text='Курс')

    class Meta:
        verbose_name = "Подписка на курс"
        verbose_name_plural = "Подписки на курс"

    def _str_(self):
        return f"Пользователь:{self.user}, Подписки: {self.course}"

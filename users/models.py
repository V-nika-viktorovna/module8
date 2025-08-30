from django.contrib.auth.models import AbstractUser
from django.db import models

from online_learning.models import Course, Lesson


class User(AbstractUser):

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=12, verbose_name='Телефон',
                             blank=True, null=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=50, verbose_name='Страна',
                               blank=True, null=True, help_text='Введите свою страну')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар',
                               blank=True, null=True, help_text='Загрузите фото для аватара')

    username = models.CharField(max_length=30, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


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

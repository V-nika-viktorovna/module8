from django.contrib.auth.models import AbstractUser
from django.db import models


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

from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Добавление пользователей в базу данных'

    def handle(self, *args, **kwargs):

        users = [
            {'email': 'test1@mail.ru'},
            {'email': 'test2@mail.ru'}
        ]

        for user_data in users:
            user, created = User.objects.get_or_create(**user_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Пользователь {user.email} добавлен'))
            else:
                self.stdout.write(self.style.WARNING(f'Пользователь {user.email} уже существует'))

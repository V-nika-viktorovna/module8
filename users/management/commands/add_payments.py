from django.core.management.base import BaseCommand

from users.models import Payments, User


class Command(BaseCommand):
    help = 'Добавление платежей в базу данных'

    def handle(self, *args, **kwargs):

        payments = [
            {'user': User.objects.get(email='test1@mail.ru'), 'payment_amount': '12000.00'},
            {'user': User.objects.get(email='test2@mail.ru'), 'payment_amount': '15000.00'}
        ]

        for payment_data in payments:
            payment, created = Payments.objects.get_or_create(**payment_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Платеж от {payment.user} на сумму \
                                                     {payment.payment_amount} добавлен'))
            else:
                self.stdout.write(self.style.WARNING('Платеж уже существует'))

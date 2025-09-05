from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def sending_emails_about_updata(email):
    """Асинхронную рассылку писем пользователям об обновлении материалов курса."""

    send_mail('Обновление курса', 'Курс из ваших подписок обновлен',
              EMAIL_HOST_USER, recipient_list=email)

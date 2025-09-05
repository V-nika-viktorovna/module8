from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def block_user():
    """Блокировка пользователя при отсутствии активности более 30 дней."""

    limit_day = timezone.now().date() - timezone.timedelta(days=30)

    active_users = User.objects.filter(is_active=True)
    for user in active_users:
        if user.last_login.date() < limit_day:
            user.is_active = False
            user.save()

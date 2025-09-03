from rest_framework.exceptions import ValidationError


def link_validator(value):
    """ Валидатор для проверки ссылки"""

    checking_link = "https://www."
    youtube = "youtube.com"

    if checking_link in value:
        if youtube not in value:
            raise ValidationError("Ссылка не может содержать сторонии ресурсы кроме YouTube")

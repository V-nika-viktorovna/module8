from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ("password",)
    list_filter = ('id', 'email', 'username', 'phone', 'country')

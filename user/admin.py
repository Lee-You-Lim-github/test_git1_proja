
from django.contrib import admin
from user.models import UserConfig


@admin.register(UserConfig)
class UserAdmin(admin.ModelAdmin):
    pass
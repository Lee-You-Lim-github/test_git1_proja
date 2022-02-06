import re

from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.models import UserConfig

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username"]

# 관리자용
class UserConfigAdminSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = UserConfig
        fields = ["id", "name", "nickname", "telephone"]

   # def validate_name(self, name):
   #     if len(name) < 3:
   #         raise serializers.ValidationError('3글자 이상!!')
   #     return name


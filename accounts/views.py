from rest_framework_simplejwt.views import (
    TokenObtainPairView as OrigTokenObtainPairView,
    TokenRefreshView as OrigTokenRefreshView,
)
from accounts.serializers import TokenObtainPairSerializer, UserCreationSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

User = get_user_model()

class SingupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]

class TokenObtainPairView(OrigTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OrigTokenRefreshView):
    pass
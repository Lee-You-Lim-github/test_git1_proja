from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from user.models import UserConfig
from user.serializers import UserConfigAdminSerializer


# list, detail, create, update, delete를 1개 ViewSet에서 지원
# 비인증 : list, detail  --(GET) // 인증 : create, update, delete
class UserConfigViewSet(viewsets.ModelViewSet):
    queryset = UserConfig.objects.all()
    serializer_class= UserConfigAdminSerializer
    # permission_classes = [AllowAny]   # DRF 디폴트 설정
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):

        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


# 저장 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    # 유효성 검사가 끝나고 나서
    # 실제 serializer.save()를 할 때 수행되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않습니다.
        # 대신 키워드 인자를 통한 속성 지원을 지원합니다.
        serializer.save(author=self.request.user)


from rest_framework import views
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import login

from utils.django.auth.serializers import LoginSerializer


class LoginView(views.APIView):
    """
    Login to the site
    """
    user_serializer_class = None
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return self.get_success_response(user, serializer)

    def get_success_response(self, user, serializer):
        if self.user_serializer_class:
            result = self.user_serializer_class(user).data
        else:
            result = {
                serializer.username_field: getattr(user, serializer.username_field)
            }
        return Response(result)

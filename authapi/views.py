from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers

from drf_spectacular.utils import extend_schema

from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class JWTResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class RegisterView(APIView):
    """
    Creates a user and returns JWT tokens when username and password are provided.
    """
    @extend_schema(
        request=RegisterSerializer,
        responses={201: JWTResponseSerializer},
        summary='Register a new user',
        description='Creates a new user account and returns JWT tokens'
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = User.objects.create_user(username=username, password=password)

        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    """
    Logs in a user and returns JWT tokens when valid credentials are provided.
    """
    @extend_schema(
        request=RegisterSerializer,
        responses=JWTResponseSerializer,
        summary='Login the user',
        description='Authenticates the user and returns JWT tokens'
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        return Response({'error': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)
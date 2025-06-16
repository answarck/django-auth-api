from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, serializers

from drf_spectacular.utils import extend_schema

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    
class RegisterView(APIView):
    @extend_schema(
        request=RegisterSerializer,
        responses={201: TokenResponseSerializer}, 
        summary='Register a new user',
        description='Creates  a new user account and returns a token'
    )
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.create(
            username=username,
            password=password
        )
        
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)




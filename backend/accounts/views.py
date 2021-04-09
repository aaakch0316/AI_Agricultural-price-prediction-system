from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import UserCreateSerializer, UserLoginSerializer

from .models import User



# Create your views here.
@api_view(['POST']) 
@permission_classes([AllowAny]) # 인증 필요없다
def signup(request):
    serializer = UserCreateSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True):
        serializer.save() # DB 저장
        return Response(serializer.data, status=201) 


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None": # email required
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'success': True,
            'token': serializer.data['token'] # 시리얼라이저에서 받은 토큰 전달
        }
        return Response(response, status=status.HTTP_200_OK)
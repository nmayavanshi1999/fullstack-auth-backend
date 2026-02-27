from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
# Create your views here.


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self , request):
        username=request.data.get("username")
        email=request.data.get("email")
        password=request.data.get("password")


        if not username or not password:
            return Response(
                {"message" : "usrname or Password required"},
                status=status.HTTP_400_BAD_REQUEST
            )



        if User.objects.filter(username=username).exists():
            return Response(
                {"message" : "usrname already exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password,

        )
        return Response(
            {"message" : "User Register succesfully"},
            status=status.HTTP_201_CREATED
        )

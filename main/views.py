from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
# Create your views here.
from .models import *


@api_view(['post'])
@permission_classes([AllowAny])
def Api_Register(request):
    username = request.data['username']
    name = request.data['name']
    lastname = request.data['lastname']
    email = request.data['email']
    password = request.data['password']

    try:
        user=User.objects.create_user(username=username,email=email,first_name=name,last_name=lastname)
        user.set_password(password)
        token = Token.objects.create(user=user)
        user.save()
        return Response({"status":True,'token':str(token)})
    except:
        return Response({"status":False})


@api_view(['post'])
@permission_classes([AllowAny])
def Api_Login(request):
    username = request.data['username']
    password = request.data['password']

    try:
        user=User.objects.get(username=username)
        if user.check_password(str(password)):
            token = Token.objects.get(user=user)
            return Response({"status":True,'token':str(token)})
        else:
            return Response({"status": None})
    except Exception as e:
        return Response({"status": False,'error':str(e)})

@api_view(['get'])
@permission_classes([IsAuthenticated])
def Api_Get_User(request):

    DATA = {
        "username":request.user.username,
        "email":request.user.email,
        "name":request.user.first_name,
        "lastname":request.user.last_name,

        }

    return Response(DATA)


def Web(request):

    return render(request, 'index.html')
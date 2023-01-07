from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i/register/', Api_Register),
    path('i/login/', Api_Login),
    path('i/getuser/', Api_Get_User),
    path('', Web),
    path('login/', Web),
    path('register/', Web),
]

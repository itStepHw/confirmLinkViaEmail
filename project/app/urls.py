from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('sign/', signIn, name='sign'),
    path('verify/', verifyUser, name='verify'),
    path('profile/', profile, name='profile'),
    path('logout/', logoutUser, name='logout'),
]
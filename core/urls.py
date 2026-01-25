from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('movie/<int:id>/', movie_detail, name='movie_detail'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]

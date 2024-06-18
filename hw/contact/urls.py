
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_category', create_category, name='create_category'),
    path('create_message', create_message, name='create_message'),
    path('congratulation', congratulation, name='congratulation'),
]
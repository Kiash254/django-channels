from django.urls import path
from .views import home

app_name = 'chats'

urlpatterns = [
    path('',home,name='home'),
]
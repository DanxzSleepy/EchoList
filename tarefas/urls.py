from django.urls import path
from . import views



urlpatterns = [
    path('', views.listatarefas, name='lista'),
]
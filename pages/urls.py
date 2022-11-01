from django.urls import path 
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('message', views.message, name='message'),
]

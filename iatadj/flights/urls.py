from django.urls import path
from flights import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
]

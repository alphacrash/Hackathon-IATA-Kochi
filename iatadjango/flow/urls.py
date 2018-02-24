from django.urls import include, path
from flow import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('profile/', views.profile),
]

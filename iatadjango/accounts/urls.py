from django.contrib import admin
from django.urls import include, path

from accounts import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]

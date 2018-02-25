from django.urls import include, path
from flow import views

urlpatterns = [
    path('', views.index),
    path('profile/', views.Profile.as_view()),
    path('home/', views.home),
    path('accept/<int:pk>', views.accepted, name="accept"),
    path('acceptor/<int:pk>', views.AcceptorView.as_view(), name='acceptor'),
    path('bumped/<int:pk>', views.bumped),
]

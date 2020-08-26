from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('genre/<str:slug>', views.SingleGenre.as_view(), name='genre'),
    path('artist/<str:slug>', views.SingleBand.as_view(), name='band'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('register/', views.register, name='register'),
    path('registration-success/', views.registration_success, name='registration_success'),
]

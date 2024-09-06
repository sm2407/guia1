from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexApp1),
    path('vista1/', views.vista1),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('minha-view/', views.minha_view, name='minha_view'),
    path('segunda-view/', views.segunda_view, name='segunda_view'),
]
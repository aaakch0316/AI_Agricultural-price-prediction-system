from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_main_price),
    path('settings/', views.add_main_price),
]
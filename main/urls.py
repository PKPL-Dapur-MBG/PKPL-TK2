from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit-style/', views.edit_style, name='edit_style'),
]
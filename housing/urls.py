from django.urls import path
from . import views

urlpatterns = [
    path('housing', views.housing, name='housing'),
    path('house/<str:pk>/', views.house, name='house'),
]

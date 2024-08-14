from django.urls import path
from . import views

urlpatterns = [
    path('academic', views.academic, name='academic'),
    path('course/<str:pk>/', views.course, name='course')
]

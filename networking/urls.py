from django.urls import path
from . import views

urlpatterns = [
    path('networking', views.networking, name='networking')
]

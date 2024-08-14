from django.urls import path
from . import views

urlpatterns = [
    path('association', views.association, name='association')
]

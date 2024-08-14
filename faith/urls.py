from django.urls import path
from . import views

urlpatterns = [
    path('faith', views.faith, name='faith')
]

from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),  
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'), 
]

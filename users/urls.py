from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import urls

from users import views

app_name = 'users'
urlpatterns = [
    path('register/',
         views.RegisterView.as_view(),
         name='register'),
    path('login/',
         LoginView.as_view(),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
]

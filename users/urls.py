from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import urls
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from users import views

app_name = 'users'
urlpatterns = [
	

	url(r'^signup/$', views.signup, name='signup'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    
    path('login/',
         LoginView.as_view(),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
]

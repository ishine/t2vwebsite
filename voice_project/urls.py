"""voice_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.shortcuts import render, redirect
from django.conf import settings

from django.urls import include, path  # For django versions from 2.0 and up



def frontpage(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
    
def about(request):
    return render(request, 'about.html')

urlpatterns = [
	path('', frontpage),
    path('login/', login),
    path('signup/', signup),
    path('about/', about),
    
    path('admin/', admin.site.urls),
    
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

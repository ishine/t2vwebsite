from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
	path('', 
		views.MainPage.as_view(), 
		name='MainPage'),
	path('create_voice/', 
		views.CreateMessageView.as_view(), 
		name='CreateVoice'),
	
]
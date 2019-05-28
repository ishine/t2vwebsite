from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [

	# Main page
	path('', 
		views.MainPage.as_view(), 
		name='MainPage'),

	# Create track
	path('create_voice/', 
		views.CreateMessageView.as_view(), 
		name='CreateVoice'),

	# Delete link 
	path('<uuid:pk>/delete/',
         views.DeleteMassageView.as_view(),
         name='delete_track'),

	path('api/voice/create/',
         views.VoiceTrackCreateView.as_view(),
         name='create_track'),

	 path('api/voice/<uuid:pk>/', 
	 	views.VoiceTrackDetail.as_view(), 
	 	name='detail_track'),

	 path('api/voice/list/', 
	 	views.VoiceTrackList.as_view(), 
	 	name='list_track'),
]
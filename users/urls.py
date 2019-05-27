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
	url(r'password_change/$',
		auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html',
			success_url='password_change_done/'),
		name='password_change'),

	url(r'password_change_done/',
		auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html')),

	url(r'password_reset/$',
		auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
			email_template_name='registration/password_reset_email.html',
			subject_template_name='registration/password_reset_subject.txt',
			success_url='password_reset_done/',
			from_email='support@yoursite.ma'),
		name='password_reset'),

	url(r'password_reset_done/',
		auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html')),

	url(r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.PasswordResetConfirmView.as_view(
			template_name='registration/password_reset_confirm.html',
			success_url='password_reset_complete/',),
		name='password_reset_confirm'),

	url(r'password_reset_complete/',
		auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html')),
]


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from captcha.fields import ReCaptchaField
# thrhr

class CustomUserCreationForm(UserCreationForm):

	captcha = ReCaptchaField()

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('email',)

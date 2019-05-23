from .forms import CustomUserCreationForm
from django.urls import reverse
from django.views.generic import CreateView
from django.conf import settings


class RegisterView(CreateView):
    template_name = 'user/signup.html'
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse(settings.LOGIN_REDIRECT_URL)
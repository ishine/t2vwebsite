from django.contrib import admin

# Register your models here.
from .models import VoiceTrack

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(VoiceTrack, AuthorAdmin)
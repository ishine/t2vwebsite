from django.contrib import admin

# Register your models here.
from .models import VoiceTrack

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'owner',] 
    list_display_links = ['id',]

admin.site.register(VoiceTrack, AuthorAdmin)
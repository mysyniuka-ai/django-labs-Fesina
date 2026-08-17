from django.contrib import admin
from .models import Platform, Genre, Game

@admin.register(Platform, Genre, Game)
class BaseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
from django.contrib import admin
from .models import Platform, Genre, Game, Review, NewsletterSubscriber

@admin.register(Platform, Genre)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'platform', 'genre', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'user_name', 'rating', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    readonly_fields = ('subscribed_at',)
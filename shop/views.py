from django.shortcuts import render
from .models import Game, Platform, Genre


def home_view(request):
    games = Game.objects.all()
    platforms = Platform.objects.all()
    genres = Genre.objects.all()

    context = {
        'title': 'Головна сторінка - GamePulse',
        'games': games,
        'platforms': platforms,
        'genres': genres,
        'is_home': True
    }
    return render(request, 'shop/base.html', context)


def platform_filter_view(request, platform_id):
    platforms = Platform.objects.all()
    genres = Genre.objects.all()
    games = Game.objects.filter(platform_id=platform_id)
    selected_platform = Platform.objects.get(id=platform_id)

    context = {
        'title': f'Платформа: {selected_platform.name}',
        'games': games,
        'platforms': platforms,
        'genres': genres,
        'selected_platform': selected_platform,
        'is_home': False
    }
    return render(request, 'shop/base.html', context)
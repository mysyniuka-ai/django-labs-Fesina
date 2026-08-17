from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Game, Platform, Genre, Review, NewsletterSubscriber, Order
from .forms import RegisterForm, ReviewForm, NewsletterForm


def home_view(request):
    games = Game.objects.all()
    platforms = Platform.objects.all()
    genres = Genre.objects.all()

    if request.method == 'POST' and 'newsletter_form' in request.POST:
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            return redirect('home')
    else:
        newsletter_form = NewsletterForm()

    context = {
        'title': 'Головна сторінка - GamePulse',
        'games': games,
        'platforms': platforms,
        'genres': genres,
        'newsletter_form': newsletter_form,
        'is_home': True
    }
    return render(request, 'shop/base.html', context)


def platform_filter_view(request, platform_id):
    platforms = Platform.objects.all()
    genres = Genre.objects.all()
    platform = get_object_or_404(Platform, id=platform_id)
    games = Game.objects.filter(platform=platform)

    context = {
        'title': f'Платформа: {platform.name}',
        'games': games,
        'platforms': platforms,
        'genres': genres,
        'selected_platform': platform,
        'is_home': False
    }
    return render(request, 'shop/category.html', context)


def game_detail_view(request, game_id):
    platforms = Platform.objects.all()
    genres = Genre.objects.all()
    game = get_object_or_404(Game, id=game_id)

    reviews = game.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST' and 'review_form' in request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.save()
            return redirect('game_detail', game_id=game.id)
    else:
        form = ReviewForm()

    context = {
        'title': game.title,
        'game': game,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'form': form,
        'platforms': platforms,
        'genres': genres,
        'is_home': False
    }
    return render(request, 'shop/game_detail.html', context)


def register_view(request):
    platforms = Platform.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form, 'platforms': platforms, 'title': 'Реєстрація'})


@login_required
def profile_view(request):
    platforms = Platform.objects.all()
    if request.user.is_staff:
        orders = Order.objects.all()  # Адмін бачить усі замовлення
    else:
        orders = Order.objects.filter(user=request.user)  # Звичайний юзер бачить тільки свої

    context = {
        'orders': orders,
        'platforms': platforms,
        'title': 'Особистий кабінет'
    }
    return render(request, 'shop/profile.html', context)
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Platform(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва платформи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name="Жанр")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва гри")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name="Платформа")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    image = models.ImageField(upload_to='games/', verbose_name="Фото товару", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews', verbose_name="Гра")
    user_name = models.CharField(max_length=50, verbose_name="Ім'я користувача")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Оцінка (1-5)")
    comment = models.TextField(verbose_name="Відгук")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.game.title} ({self.rating}/5)"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email для розсилки")
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    product_name = models.CharField(max_length=100, verbose_name="Товар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")

    def __str__(self):
        return f"Замовлення #{self.id} — {self.user.username}"
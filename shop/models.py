from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return self.title
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('platform/<int:platform_id>/', views.platform_filter_view, name='platform_filter'),
]
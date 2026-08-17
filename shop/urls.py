from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('page1/', views.page_one_view, name='page1'),
    path('page2/', views.page_two_view, name='page2'),
]
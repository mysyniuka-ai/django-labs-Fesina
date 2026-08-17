from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Review, NewsletterSubscriber

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email адреса")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
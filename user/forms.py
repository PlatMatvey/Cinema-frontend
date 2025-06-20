from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.Textarea)

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    text = forms.CharField(max_length=255)

class RatingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    rating = forms.IntegerField()


class CreateChatForm(forms.Form):
    users = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Выберите участников',
        required=False
    )

class CreateMessageForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Введите сообщение...',
            'rows': 3,
            'class': 'form-control'
        }),
        max_length=1000,
        required=True,
        label='Сообщение'
    )
    created_at = forms.DateTimeField(
        widget=forms.HiddenInput(),
        initial=timezone.now,
        required=False
    )
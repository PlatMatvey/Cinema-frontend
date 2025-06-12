from django import forms
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
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите участников'
    )

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label="Введите логин")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label="Повторите пароль")
    age = forms.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], label="Введите свой возраст")
    subscribe = forms.BooleanField(required=False, label="Подписаться на рассылку")
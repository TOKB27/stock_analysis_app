from django import forms
from accounts.models import CustomUser
import re

class AuthForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password',)
        labels = {'username': 'ユーザID', 'password': 'パスワード'}
        widgets = {'password': forms.PasswordInput, }

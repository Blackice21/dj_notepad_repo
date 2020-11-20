from django import forms
from .models import Note
from django.contrib.auth.models import User

class Noteform(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']



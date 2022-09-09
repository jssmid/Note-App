from pydoc import text
from django.forms import ModelForm
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note']


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
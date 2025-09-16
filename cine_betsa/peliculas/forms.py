from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Pelicula
from django import forms

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'genero', 'director', 'anio']


class RegistrarUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        from .models import Pelicula

    class PeliculaForm(forms.ModelForm):
        class Meta:
            model = Pelicula
            fields = '__all__'


from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import RegistrarUsuarioForm
from .forms import PeliculaForm
from .models import Pelicula
from django.contrib.auth.decorators import login_required

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listaspeliculas')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'registrar.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('listaspeliculas')
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})

    @login_required
    def registrar_pelicula(request):
        if request.method == 'POST':
            form = PeliculaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('listaspeliculas')
            else:
                form = PeliculaForm()
                return render(request, 'registrar_pelicula.html', {'form': form})
    def lista_peliculas(request):
        peliculas = Pelicula.objects.all()
        return render(request, 'listaspeliculas.html', {'peliculas': peliculas})



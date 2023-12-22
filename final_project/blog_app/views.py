from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import *

# Create your views here.

def home_view(request):

    return render(request, 'blog_app/home.html', {'user':request.user})

def login_view(request):

    if request.user.is_authenticated:
        return redirect('blog_app:home')

    if request.method == "GET":
        return render(
            request,
            "blog_app/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "blog_app/home.html",
                {"mensaje": f"Bienvenido {modelo.username}"}
            )
        else:
            return render(
                request,
                "blog_app/login.html",
                {"form": formulario}
            )

def register_view(request):

    if request.method == "GET":
        return render(
            request,
            "blog_app/register.html",
            {"form": RegisterForm()}
        )
    else:
        formulario = RegisterForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "blog_app/login.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "blog_app/register.html",
                {"form": formulario}
            )

def logout_view(request):

    logout(request)
    return redirect('blog_app:login_user')

def profile_view(request):

    return render(request, 'blog_app/profile.html')
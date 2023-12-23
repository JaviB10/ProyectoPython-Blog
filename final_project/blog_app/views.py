from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.http import HttpResponse
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

            return redirect('blog_app:home')
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
    return redirect('blog_app:home')

def profile_view(request):
    return render(request, 'blog_app/profile.html')

class CategoryListView(ListView):
    model = Category
    template_name = 'blog_app/category.html'  # Reemplaza con la ruta correcta a tu template
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog_app/category_create.html'  # Reemplaza con la ruta correcta a tu template
    success_url = reverse_lazy('blog_app:category_list')  # Reemplaza con el nombre de tu URL de éxito

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponse("Error: This category already exists.")

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog_app/category_update.html'  # Reemplaza con la ruta correcta a tu template
    success_url = reverse_lazy('blog_app:category_list')  # Reemplaza con el nombre de tu URL de éxito

    def form_valid(self, form):
        # Puedes agregar lógica adicional aquí si es necesario
        return super().form_valid(form)

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'blog_app/category_delete.html'  # Reemplaza con la ruta correcta a tu template
    success_url = reverse_lazy('blog_app:category_list')  # Reemplaza con el nombre de tu URL de éxito
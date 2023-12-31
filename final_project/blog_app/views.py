from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .forms import *

# Create your views here.
# Vistas basadas en funciones
def home_view(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog_app/home.html', {'user': request.user, 'articles': articles, 'categories': categories})

def about_view(request):
    return render(request, 'blog_app/about.html', {'user': request.user})

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
    if request.user.is_authenticated:
        return redirect('blog_app:home')

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

            return redirect('blog_app:login_user')
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

# Vistas basadas en clases
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'blog_app/user_list.html'
    context_object_name = 'users'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'blog_app/user_update.html'
    success_url = reverse_lazy('blog_app:profile_user')
    
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponse('The username is already in use. Please choose a different one.')

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'blog_app/user_delete.html'
    success_url = reverse_lazy('blog_app:home')

@method_decorator(login_required, name='dispatch')
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'blog_app/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Devuelve el perfil asociado al usuario actual
        return self.request.user.profile

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'blog_app/profile_update.html'
    success_url = reverse_lazy('blog_app:profile_user')

    def form_valid(self, form):
        # Llama al método padre para que realice la actualización estándar
        response = super().form_valid(form)
        return response

class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = 'blog_app/avatar_update.html'
    success_url = reverse_lazy('blog_app:profile_user')  
    
    def get_object(self, queryset=None):
        # Devuelve el objeto que se actualizará, en este caso, el avatar del usuario actual
        return Avatar.objects.get(user=self.request.user)

    def form_valid(self, form):
        # Verifica si la casilla 'clear' está marcada
        if form.cleaned_data['clear']:
            avatar = get_object_or_404(Avatar, user=self.request.user)
            avatar.image.delete()  # Elimina el archivo de la imagen actual
            avatar.image = '/default_avatar.png'  # Establece la ruta del avatar predeterminado
            avatar.save()
            return HttpResponseRedirect(self.get_success_url())  # Redirige sin procesar el formulario
        return super().form_valid(form)

class CategoryListView(ListView):
    model = Category
    template_name = 'blog_app/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog_app/category_create.html'
    success_url = reverse_lazy('blog_app:category_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponse("Error: This category already exists.")

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog_app/category_update.html'
    success_url = reverse_lazy('blog_app:category_list')

    def form_valid(self, form):
        return super().form_valid(form)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'blog_app/category_delete.html'
    success_url = reverse_lazy('blog_app:category_list')

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'blog_app/article_list.html'
    context_object_name = 'articles'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog_app/article_create.html'
    success_url = reverse_lazy('blog_app:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'blog_app/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        # Obtén el ID del artículo de la URL
        article_id = self.kwargs['pk']
        # Filtra la consulta por el ID del artículo
        return Article.objects.get(id=article_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtén los comentarios asociados al artículo
        comments = Comment.objects.filter(article=self.object, is_approved=True)
        context['comments'] = comments
        return context

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'blog_app/article_delete.html'
    success_url = reverse_lazy('blog_app:article_list')

class ArticleCategoryListView(ListView):
    model = Article
    template_name = 'blog_app/article_category_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        # Obtén la categoría basada en el slug
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        
        # Filtra los artículos por la categoría
        return Article.objects.filter(categories=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega la categoría al contexto para usarla en la plantilla
        context['category'] = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog_app/comment_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['article'] = article
        return context

    def form_valid(self, form):
        # Asocia el comentario con el artículo y el autor
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirige a la página de detalles del artículo después de agregar un comentario
        return reverse('blog_app:article_detail', kwargs={'pk': self.kwargs['pk']})

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'blog_app/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        # Filtra los mensajes por el usuario actual como remitente o destinatario
        return Message.objects.filter(sender=self.request.user) | Message.objects.filter(receiver=self.request.user)

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'blog_app/message_create.html'
    success_url = reverse_lazy('blog_app:message_list')

    def get_form_kwargs(self):
        kwargs = super(MessageCreateView, self).get_form_kwargs()
        # Pasa el usuario logueado como el remitente al formulario
        kwargs['sender'] = self.request.user

        return kwargs

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
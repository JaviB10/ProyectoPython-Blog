from django.urls import path
from blog_app.views import *

app_name = 'blog_app'

urlpatterns = [
    # Páginas principales
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),

    # Autenticación de usuarios
    path('login/', login_view, name='login_user'),
    path('register/', register_view, name='register_user'),
    path('logout/', logout_view, name='logout_user'),

    # Categorías
    path('category/add', CategoryCreateView.as_view(), name='category_created'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/list', CategoryListView.as_view(), name='category_list'),

    # Perfil de usuario
    path('profile/', UserProfileDetailView.as_view(), name='profile_user'),
    path('profile/update/<int:pk>/', UserProfileUpdateView.as_view(), name='profile_update'),

    # Usuarios
    path('user/list', UserListView.as_view(), name='user_list'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    # Avatar
    path('avatar/update/<int:pk>/', AvatarUpdateView.as_view(), name='avatar_update'),

    # Artículos
    path('article/add', ArticleCreateView.as_view(), name='article_created'),
    path('article/list', ArticleListView.as_view(), name='article_list'),
    path('article/detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),

    # Comentarios
    path('comment/add/<int:pk>/', CommentCreateView.as_view(), name='comment_created'),

    # Artículos por categoría
    path('category/<slug:category_slug>/', ArticleCategoryListView.as_view(), name='article_category_list'),

    # Mensajes
    path('message/add', MessageCreateView.as_view(), name='message_created'),
    path('message/list', MessageListView.as_view(), name='message_list'),
]

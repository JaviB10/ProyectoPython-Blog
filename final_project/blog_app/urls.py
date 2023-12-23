from django.urls import path
from blog_app.views import *

app_name = 'blog_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login_user'),
    path('register/', register_view, name='register_user'),
    path('logout/', logout_view, name='logout_user'),
    path('category/add', CategoryCreateView.as_view(), name='category_created'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/list', CategoryListView.as_view(), name='category_list'),
]

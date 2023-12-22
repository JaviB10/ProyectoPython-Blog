from django.urls import path
from blog_app.views import *

app_name = 'blog_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login_user'),
    path('register/', register_view, name='register_user'),
    path('logout/', logout_view, name='logout_user'),
]

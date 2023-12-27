from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Avatar)
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
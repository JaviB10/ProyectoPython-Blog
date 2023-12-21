from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.

class User(AbstractUser):

    # Campos adicionales
    date_of_birth = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Asignar el rol de administrador al usuario
        self.is_staff = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="media/avatars", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.image}"

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2200)
    website = models.URLField(blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username}'

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        # Generar automáticamente el slug basado en el nombre
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Generar automáticamente el slug basado en el título
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.article.title}'
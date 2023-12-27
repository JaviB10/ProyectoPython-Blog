from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
# Modelos relacionados con la autenticación de usuarios
class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Avatar(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True, default='default_avatar.png')

    def save(self, *args, **kwargs):
        # Si el campo image está vacío, asigna la imagen predeterminada
        if not self.image:
            self.image = 'default_avatar.png'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.image}"

@receiver(post_save, sender=User)
def create_user_avatar(sender, instance, created, **kwargs):
    if created:
        Avatar.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_avatar(sender, instance, **kwargs):
    try:
        instance.avatar.save()
    except Avatar.DoesNotExist:
        # Si no hay avatar, no hay nada que guardar
        pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=2200, default='')
    website = models.URLField(blank=True, default='')

    def __str__(self):
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        # Si no hay perfil, no hay nada que guardar
        pass

# Modelos relacionados con el intercambio de mensajes
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username}'

# Otros modelos relacionados con la aplicación
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

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, max_length=500)
    short_content = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generar automáticamente el slug basado en el título
        if not self.slug:
            self.slug = slugify(self.title)

        # Si short_content no se ha establecido manualmente, generarlo a partir de los primeros 100 caracteres del contenido
        if not self.short_content:
            self.short_content = self.content[:100]

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
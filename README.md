# Proyecto Django: Blog App

## BLOG GAMES

Comisión: 47790

Alumno: Javier Ballón

## Estructura del Proyecto

```bash
final_project/
├── blog_app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── blog_app/
│   │       ├── article_create.html
│   │       ├── article_detail.html
│   │       ├── article_list.html
│   │       ├── base_generic.html
│   │       ├── category_create.html
│   │       ├── category_delete.html
│   │       ├── category_list.html
│   │       ├── category_update.html
│   │       ├── comment_create.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── message_create.html
│   │       ├── message_list.html
│   │       ├── profile.html
│   │       ├── profile_update.html
│   │       ├── register.html
│   │       ├── user_delete.html
│   │       ├── user_list.html
│   │       └── user_update.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── final_project/
│    ├── __init__.py
│    ├── asgi.py
│    ├── settings.py
│    ├── urls.py
│    └── wsgi.py
└── media/
│    └── avatars/
├── manage.py
```

## Configuración del Proyecto

### Modelos:

    - User: Modelo personalizado de usuario con campos adicionales.
    - Avatar: Modelo para el avatar de usuario.
    - Profile: Modelo para el perfil de usuario.
    - Message: Modelo para mensajes internos.
    - Author, Category, Article, Comment: Modelos para la funcionalidad de blog.

## Vistas:

### Vistas: 
    - Login
    - Register
    - Profile
    - Messages
    - Categories
    - Articles

## Formularios:

Formularios personalizados para autenticación, registro, categorías, perfil, usuario, avatar, artículo, comentario y mensajes.

## URLs:

Configuración de las URL para todas las vistas de la aplicación.

## Tecnología Utilizada

### Frontend

    - HTML
    - CSS
    - Javascript
    - Bootstrap

### Backend

    - Python
    - Django

## Video demostración

https://youtu.be/SPO-arOxM-M

## Ejecución del Proyecto

### Instala las dependencias:

```bash
pip install -r requirements.txt
```

### Aplica las migraciones:

```bash
python manage.py migrate
```

### Crea un superusuario:

```bash
python manage.py createsuperuser
```

### Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

Accede al panel de administración en http://127.0.0.1:8000/admin/ para gestionar usuarios, categorías, artículos, etc.

Explora la aplicación en http://127.0.0.1:8000/.

¡Disfruta construyendo tu blog con Django! Si tienes alguna pregunta o encuentras algún problema, no dudes en preguntar. ¡Buena codificación!
# Proyecto Django: Blog App

## ¡Bienvenido al repositorio de la aplicación Django "Blog App"! Este proyecto es una aplicación de blog con características como autenticación de usuarios, perfiles, categorías, artículos, comentarios y mensajería interna.

0. Estructura del Proyecto
plaintext
Copy code
```bash
tu_proyecto/
├── blog_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
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
│   ├── tests/
│   ├── urls.py
│   └── views.py
├── manage.py
└── tu_proyecto/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

1. Configuración del Proyecto

```bash
Modelos:

User: Modelo personalizado de usuario con campos adicionales.
Avatar: Modelo para el avatar de usuario.
Profile: Modelo para el perfil de usuario.
Message: Modelo para mensajes internos.
Author, Category, Article, Comment: Modelos para la funcionalidad de blog.
```

2. Vistas:

Vistas para la página de inicio, registro, inicio de sesión, perfil, categorías, artículos y mensajes.

3. Formularios:

Formularios personalizados para autenticación, registro, categorías, perfil, usuario, avatar, artículo, comentario y mensajes.

4. URLs:

Configuración de las URL para todas las vistas de la aplicación.

5. Ejecución del Proyecto
Instala las dependencias:

```bash
Copy code
pip install -r requirements.txt
```

Aplica las migraciones:
```bash
Copy code
python manage.py migrate
```

Crea un superusuario:
```bash
Copy code
python manage.py createsuperuser
```

Ejecuta el servidor de desarrollo:
```bash
Copy code
python manage.py runserver
```

Accede al panel de administración en http://127.0.0.1:8000/admin/ para gestionar usuarios, categorías, artículos, etc.

Explora la aplicación en http://127.0.0.1:8000/.

¡Disfruta construyendo tu blog con Django! Si tienes alguna pregunta o encuentras algún problema, no dudes en preguntar. ¡Buena codificación!
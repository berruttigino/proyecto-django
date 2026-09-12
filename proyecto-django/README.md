# Workshop - Proyecto Final Django

Aplicación web desarrollada con Django que gestiona publicaciones (posts) de un blog, integrando herencia de templates, formularios con búsqueda dinámica, panel de administración personalizado y gestión de usuarios con permisos.

## Requisitos

- Python 3.10+
- pip

## Instalación

1. Cloná el repositorio o descomprimí el ZIP:
```bash
   git clone <url-del-repositorio>
   cd proyecto-django
```

2. Creá y activá un entorno virtual:
```bash
   python -m venv env
   # En Windows (PowerShell):
   .\env\Scripts\Activate.ps1
```

3. Instalá las dependencias:
```bash
   pip install -r requirements.txt
```

## Migraciones y datos de ejemplo

1. Aplicá las migraciones:
```bash
   python manage.py migrate
```

2. Creá un superusuario:
```bash
   python manage.py createsuperuser
```

3. Cargá datos de ejemplo desde el admin (`/admin/`) o mediante la interfaz pública creando posts desde "+ Nuevo post".

## Ejecución

```bash
python manage.py runserver
```

La aplicación queda disponible en `http://127.0.0.1:8000/`.

## Funcionalidades

- **CRUD de Posts**: listado, detalle, creación, edición y eliminación (`/posts/`).
- **Herencia de templates**: `base.html` define bloques `title`, `nav` y `content`, extendido por `post_list.html`, `post_detail.html`, `post_form.html` y `post_confirm_delete.html`.
- **Búsqueda dinámica**: formulario en el listado que filtra posts por título usando `icontains` (`/posts/?q=<texto>`).
- **Panel de administración personalizado**: `ModelAdmin` para Author, Tag y Post con `list_display`, `list_filter` y `search_fields`.
- **Gestión de usuarios y permisos**: grupo "Editores" con permisos de solo ver y cambiar publicaciones (sin agregar ni eliminar).

## Cómo probar

- Ingresá a `/admin/` con el superusuario para gestionar todos los modelos.
- Ingresá a `/posts/` para ver el listado público, usar la búsqueda y probar el CRUD.
- Iniciá sesión con un usuario del grupo "Editores" para comprobar el acceso restringido (solo ver/editar publicaciones).

## Pruebas automatizadas

Ejecutar con:
```bash
python manage.py test
```

## Estructura del proyecto

```
proyecto-django/
├── config/          # Configuración del proyecto Django
├── core/            # App principal: modelos Author, Tag, Post
│   ├── templates/core/
│   ├── static/core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   └── urls.py
├── manage.py
└── requirements.txt
```
# Módulo 6 - Django Básico

## Descripción
Este módulo contiene la aplicación base en **Django**, que sirve como proyecto inicial para practicar la creación de aplicaciones web con Python.  
Se establece la estructura del proyecto, se configuran las aplicaciones y se prepara el entorno para desarrollos posteriores.

## Cómo ejecutar
1. Activar el entorno virtual:
   ```bash
   django_env\Scripts\activate

2. Instalar dependencias:
pip install -r requirements.txt (genera requirements con `pip freeze > requirements.txt`)

3. Ejecutar migraciones:
python manage.py migrate

4. Crear superusuario (opcional, para administración):
python manage.py createsuperuser

5. Iniciar servidor:
python manage.py runserver

6. Abrir en navegador:
http://127.0.0.1:8000/

Funcionalidades implementadas

Proyecto base en Django con estructura de apps.
Configuración de base de datos SQLite por defecto.
Preparación del entorno para desarrollo y pruebas posteriores.


# Módulo 7 - Django - BD

## Descripción
Este módulo es la continuación del proyecto del Módulo 6 y tiene como objetivo fortalecer la aplicación Django agregando funcionalidades completas de CRUD y seguridad.

Se incluyen mejoras como:

Sistema de autenticación completo (login y logout).
Protección de vistas mediante @login_required.
Estructuración correcta de URLs y navegación.
Creación y edición de tareas mediante formularios personalizados.
Vistas basadas en funciones y plantillas organizadas.

Con estas mejoras, la aplicación funciona como un CRUD seguro, organizado y listo para integrar al portafolio.

## Funcionalidades implementadas

Registro, edición y eliminación de tareas.
Visualización de tareas asociadas a cada usuario.
Sistema de login y logout con acceso protegido.
Formularios personalizados para creación y edición de tareas.
Navegación clara entre vistas y plantillas.

## Cómo ejecutar

Seguir los mismos pasos que en el Módulo 6, asegurándose de tener migraciones actualizadas y superusuario creado.

## Mejoras aplicadas

Refactorización de URLs y vistas para mayor claridad.
Protección de rutas y seguridad en la gestión de tareas.
Plantillas y formularios más organizados y reutilizables.
Código comentado para facilitar comprensión y mantenimiento.

Autor
Paulina Huentel
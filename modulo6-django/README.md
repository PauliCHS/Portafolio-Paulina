# Módulo 6 - Django básico

Cómo ejecutar:
1. Activar entorno virtual
2. pip install -r requirements.txt   (genera requirements con `pip freeze > requirements.txt`)
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver

# Módulo 7 - Django - BD

Este módulo corresponde a la continuación del trabajo realizado en el Módulo 6. Partiendo de la aplicación base desarrollada previamente en Django, en el Módulo 7 se incorporaron mejoras y requisitos adicionales para fortalecer el proyecto. Entre las optimizaciones realizadas se incluyen: implementación completa del sistema de autenticación (login y logout), protección de vistas mediante @login_required, estructuración correcta de URLs, creación y edición de tareas mediante formularios personalizados, vistas basadas en funciones y plantillas más organizadas.

Con estas mejoras, la aplicación ahora funciona como un CRUD completo, seguro y listo para integrar al portafolio. Este módulo consolida lo aprendido previamente y da continuidad natural al desarrollo del proyecto iniciado en el Módulo 6.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista'),
    path('crear/', views.crear_tarea, name='crear'),
    path('editar/<int:pk>/', views.editar_tarea, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_tarea, name='eliminar'),
]

from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'estado', 'fecha')
    list_filter = ('estado', 'fecha')
    search_fields = ('titulo', 'descripcion')

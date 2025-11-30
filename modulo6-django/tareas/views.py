from django.shortcuts import render

def index(request):
    return render(request, "tareas/index.html", {'mensaje': 'Bienvenida Paulina - Gestor de Tareas'})


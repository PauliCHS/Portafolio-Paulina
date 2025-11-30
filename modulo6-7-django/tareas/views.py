from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'tareas/lista.html', {'tareas': tareas})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('lista')
    else:
        form = TareaForm()
    return render(request, 'tareas/form.html', {'form': form, 'accion': 'Crear'})

@login_required
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/form.html', {'form': form, 'accion': 'Editar'})

@login_required
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista')
    return render(request, 'tareas/confirm_delete.html', {'tarea': tarea})

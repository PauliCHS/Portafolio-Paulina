from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    fecha = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha', 'estado']

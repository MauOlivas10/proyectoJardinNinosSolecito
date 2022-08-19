from django import forms
from .models import Contacto, Entregables
from django.forms import ModelForm, ClearableFileInput



class CustomClearableFieldInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model = Entregables
        fields = ['nombreAlumno', 'grupo', 'correo', 'nota', 'archivo']
        widgets = {
            'archivo': CustomClearableFieldInput
        }


class ContactoForm(forms.ModelForm):
    class Meta:
        model= Contacto
        fields = ['nombreP', 'nombreA', 'telefono', 'grupo', 'correo', 'duda']

class ContacoFormDuda(forms.ModelForm):
    class Meta:
        model= Contacto
        fields = ['duda']

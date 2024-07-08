# TopoWeb/forms.py

from django import forms

class MiFormulario(forms.Form):
    # Definir campos del formulario aquí
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)  # Campo de tipo Textarea para el mensaje
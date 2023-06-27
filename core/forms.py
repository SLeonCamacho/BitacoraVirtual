from django.forms import forms
from .models import Ingreso

class IngresoFormulario(forms.ModelForm):
    class Meta:
        model=Ingreso
        
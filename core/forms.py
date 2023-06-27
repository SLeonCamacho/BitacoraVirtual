from django.forms import ModelForm, CharField
from .models import Ingreso

class IngresoFormulario(ModelForm):
    motivo=CharField(max_length=20)
    class Meta:
        model=Ingreso
        exclude=("timestamp",)
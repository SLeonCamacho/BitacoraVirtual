from django.shortcuts import render
from .forms import IngresoFormulario
# Create your views here.
def vista_formulario(request):
    if request.method=="POST":
        form = IngresoFormulario(request.POST)
        pass
    form = IngresoFormulario()
    return render(request,'core/formulario_ingreso.html',{"form":form})
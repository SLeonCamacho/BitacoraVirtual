from django.shortcuts import render

# Create your views here.
def vista_formulario(request):
    if request.method=="POST":
        pass
    return render('core/formulario_ingreso.html',{})
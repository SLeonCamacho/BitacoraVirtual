from django.shortcuts import render, redirect
from django.forms import inlineformset_factory, modelform_factory
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListAPIView
from django.contrib.auth import authenticate, login, logout
from core.serializers import IngresoSerializer
from .models import Ingreso, Persona


@login_required(login_url='/')
def vista_formulario(request):
    persona_form = modelform_factory(Persona, fields='__all__')
    persona = Persona()
    ingreso_form = inlineformset_factory(
        Persona, Ingreso, fields='__all__', extra=1, can_delete=False)
    if request.method == "POST":
        data_persona_form = persona_form(request.POST)
        data_ingreso_form = ingreso_form(request.POST)
        if (not data_persona_form.is_valid()) or (not data_ingreso_form.is_valid()):
            return render(request, 'core/formulario_ingreso.html', {"persona_form": data_persona_form, "ingreso_form": data_ingreso_form})
        persona, creado = Persona.objects.get_or_create(
            **data_persona_form.cleaned_data)
        data_ingreso_form = ingreso_form(request.POST, instance=persona)
        data_ingreso_form.save()
        return render(request, 'core/formulario_ingreso.html',
                      {"persona_form": persona_form, "ingreso_form": ingreso_form, 'mensaje': "Visita registrada"})
    return render(request, 'core/formulario_ingreso.html', {"persona_form": persona_form, "ingreso_form": ingreso_form(instance=persona)})


@login_required(login_url='/')
def vista_lista(request):
    return render(request, 'core/lista_ingresos.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            error_message = 'Credenciales inválidas'
            return render(request, "core/login.html", {'error_message': error_message})
        login(request, user)
        if user.is_staff:
            return redirect('vista_list')
        return redirect('vista_formulario')

    return render(request, "core/login.html")


def logout_view(request):
    logout(request)
    return redirect('vista_login')


class IngresoVistaLista(ListAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer

    class Meta:
        model = Ingreso

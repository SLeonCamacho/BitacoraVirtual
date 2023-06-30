from django.shortcuts import render
from django.forms import inlineformset_factory, modelform_factory

from .models import Ingreso, Persona


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
        persona, creado = Persona.objects.get_or_create(**data_persona_form.cleaned_data)
        data_ingreso_form = ingreso_form(request.POST,instance=persona)
        data_ingreso_form.save()
        return render(request, 'core/formulario_ingreso.html',
                      {"persona_form": persona_form, "ingreso_form": ingreso_form, 'mensaje': "Visita registrada"})

    return render(request, 'core/formulario_ingreso.html', {"persona_form": persona_form, "ingreso_form": ingreso_form(instance=persona)})

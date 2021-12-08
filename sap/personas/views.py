from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import PersonaForm
from personas.models import Persona


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    personaEncontrada = get_object_or_404(Persona, pk=id)
    persona = {'persona': personaEncontrada}
    return render(request, 'personas/detalle.html', persona)

# PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:
        formaPersona = PersonaForm()
    persona = {'formaPersona': formaPersona}
    return render(request, 'personas/nuevo.html', persona)

def editarPersona(request, id):
    personaEncontrada = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=personaEncontrada)
        if formaPersona.is_valid():
            formaPersona.save() # Django reconoce cuando es un insert o un update
            return redirect('inicio')
    else:
        formaPersona = PersonaForm(instance=personaEncontrada)
    persona = {'formaPersona': formaPersona}
    return render(request, 'personas/editar.html', persona)

def eliminarPersona(request, id):
    personaEncontrada = get_object_or_404(Persona, pk=id)
    if personaEncontrada:
        personaEncontrada.delete()
    return redirect('inicio')

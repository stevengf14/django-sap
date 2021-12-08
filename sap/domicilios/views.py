from django.shortcuts import render, get_object_or_404, redirect
from domicilios.models import Domicilio
from domicilios.forms import DomicilioForm

# Create your views here.

def detalleDomicilio(request, id_domicilio):
    domicilioEncontrado = get_object_or_404(Domicilio, id=id_domicilio)
    domicilio = {'domicilio': domicilioEncontrado}
    return render(request, 'domicilios/detalle.html', domicilio)


def nuevoDomicilio(request):
    if request.method =='POST':
        formaDomicilio = DomicilioForm(request.POST)
        persona = {'formaPersona': formaDomicilio}
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('domicilios')
    else:
        formaDomicilio = DomicilioForm()
        domicilio = {'formaDomicilio': formaDomicilio}
    return render(request, 'domicilios/nuevo.html', domicilio)

def editarDomicilio(request, id_domicilio):
    domicilioEncontrado = get_object_or_404(Domicilio, pk=id_domicilio)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilioEncontrado)
        persona = {'formaPersona': formaDomicilio}
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('domicilios')
    else:
        formaDomicilio = DomicilioForm(instance=domicilioEncontrado)
        domicilio = {'formaDomicilio': formaDomicilio}
    return render(request, 'domicilios/editar.html', domicilio)

def eliminarDomicilio(request, id_domicilio):
    domicilioEncontrado = get_object_or_404(Domicilio, pk=id_domicilio)
    if domicilioEncontrado:
        domicilioEncontrado.delete()
    return redirect('domicilios')
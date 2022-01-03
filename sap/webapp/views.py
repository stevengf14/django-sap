from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona, Domicilio

def bienvenido(request):
    no_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    # Ordenar personas
    # Descendente -- personas = Persona.objects.order_by('-id')
    # Varios campos -- personas = Persona.objects.order_by('-id', 'nombre')
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas})

def domicilios(request):
    domicilios = {'domicilios': Domicilio.objects.order_by('id')}
    return render(request, 'domicilios.html', domicilios)
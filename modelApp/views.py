from django.shortcuts import render
from modelApp.models import Persona
from modelApp.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def listaPersonas(request):
    #Select * FROM persona
    Personas = Persona.objects.all()
    data = {
        'personas' : Personas
    }
    return render(request, 'modelApp/personas.html', data)

def crearPersona(request):
    form = PersonaForm()

    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            print("El formulario es valido")
            form.save()
            return HttpResponseRedirect(reverse("lista_personas"))

    data = {'form': form}
    return render(request, 'modelApp/personaForm.html',data)


def eliminarPersona(request, id):
    """ Buscar la persona cuyo id corresponda """
    persona = Persona.objects.get(id = id)
    persona.delete()
    return HttpResponseRedirect(reverse("lista_personas"))

def editarPersona(request, id):
    """ Rescatar los datos de la persona que queremos editar """
    persona = Persona.objects.get(id = id)
    """ Le pasamos los datos al formulario """
    form = PersonaForm(instance=persona)

    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            print("El formulario es valido")
            form.save()
            return HttpResponseRedirect(reverse("lista_personas"))

    data = {'form': form}
    return render(request, 'modelApp/personaForm.html',data)
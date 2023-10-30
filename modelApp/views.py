from django.shortcuts import render
from modelApp.models import Persona

# Create your views here.
def listaPersonas(request):
    #Select * FROM persona
    Personas = Persona.objects.all()
    data = {
        'personas' : Personas
    }
    return render(request, 'modelApp/personas.html', data)
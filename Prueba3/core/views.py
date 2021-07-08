from core.models import Carrusel
from django.shortcuts import render

# Create your views here.


def index(request):
    carruselCompleto = Carrusel.objects.all()
    datos = {
        "carruselCompleto": carruselCompleto
    }
    

    return render(request, 'core/index.html', datos)

def trabajos(request):

    return render(request, 'core/trabajos.html')

def acercade(request):

    return render(request, 'core/acercade.html')

def formulario(request):

    return render(request, 'core/formulario.html')

def api(request):

    return render(request, 'core/api.html')



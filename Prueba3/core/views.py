from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'core/index.html')

def trabajos(request):

    return render(request, 'core/trabajos.html')

def acercade(request):

    return render(request, 'core/acercade.html')

def formulario(request):

    return render(request, 'core/formulario.html')

def api(request):

    return render(request, 'core/api.html')



from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'core/index.html')

def trabajos(request):

    return render(request, 'core/trabajos.html')


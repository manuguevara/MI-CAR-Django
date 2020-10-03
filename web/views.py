from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'web/home.html')

def galeria(request):
    return render(request, 'web/galeria.html')
    
def insumos(request):
    return render(request, 'web/insumos.html')

def misionvision(request):
    return render(request, 'web/misionvision.html')

def registro(request):
    return render(request, 'web/registro.html')

def ubicacion(request):
    return render(request, 'web/ubicacion.html')
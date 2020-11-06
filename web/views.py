from django.shortcuts import render, redirect, get_object_or_404
from .models import Slider, Galeria, MisionVision, Insumo
from .forms import CustomUserCreationForm, InsumoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def home(request):
    sliders = Slider.objects.all()

    data = {
        "sliders" : sliders
    }
    return render(request, 'web/home.html', data)

def galeria(request):
    galeria = Galeria.objects.all()

    data = {
        "galeria" : galeria
    }
    return render(request, 'web/galeria.html', data)

def misionvision(request):
    misionvision = MisionVision.objects.all()

    data = {
        "misionvision" :  misionvision
    }
    return render(request, 'web/misionvision.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def ubicacion(request):
    return render(request, 'web/ubicacion.html')

@permission_required('web.add_insumo')
def agregar_insumo(request):

    data = {
        'form' : InsumoForm()
    }
    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
            messages.success(request, "Guardado correctamente")
        else:
            data["form"] = formulario
    return render(request, 'web/insumos/agregar.html', data)

@permission_required('web.view_insumo')
def listar_insumos(request):
    insumos = Insumo.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(insumos, 5)
        insumos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : insumos,
        'paginator' : paginator
    }
    return render(request,'web/insumos/listar.html', data)

@permission_required('web.change_insumo')
def modificar_insumo(request, id):
    
    insumo = get_object_or_404(Insumo, id=id)

    data = {
        'form' : InsumoForm(instance=insumo)
    }

    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST, instance=insumo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_insumos")
        data["form"] = formulario

    return render(request,'web/insumos/modificar.html',data)

@permission_required('web.delete_insumo')
def eliminar_insumo(request, id):
    insumo = get_object_or_404(Insumo, id=id)
    insumo.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_insumos") 

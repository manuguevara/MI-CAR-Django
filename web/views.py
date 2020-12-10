from django.shortcuts import render, redirect, get_object_or_404
from .models import Slider, Galeria, MisionVision, Insumo, Contacto
from .forms import CustomUserCreationForm, InsumoForm, ContactoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import InsumoSerializer, TokenSerializer, ContactoSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from fcm_django.models import FCMDevice
from django.contrib.auth.models import User

# Create your views here.
@api_view(["POST"])
def save_token(request):
    serializador = TokenSerializer(data=request.data)
    if serializador.is_valid():
        token = serializador.data["token"]

        dispositivo = FCMDevice.objects.filter(registration_id=token, active=True).first()

        if not dispositivo:
            dispositivo = FCMDevice(registration_id=token, active=True)

        if request.user.is_authenticated:
            dispositivo.user = request.user
        dispositivo.save()

        return JsonResponse({"mensaje" : "ok"}, status=200)
    return JsonResponse({"mensaje" : "no viene el token"}, status=400)#badrequest


def error_facebook(request):
    return render(request, 'registration/error_facebook.html')

class ContactoViewset(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class InsumoViewset(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer

    def get_queryset(self):
        insumos = Insumo.objects.all()
        nombre = self.request.GET.get('nombre')
        stock = self.request.GET.get('stock')
        if nombre:
            insumos = insumos.filter(nombre__contains=nombre)
        if stock:
            insumos = insumos.filter(stock=stock)
        return insumos

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

def contacto(request):
    data = {
        'form' : ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
            messages.success(request, "Solicitud enviada correctamente")
            nombre_contacto = formulario.cleaned_data["nombre"]
            usuarios = list(User.objects.all().filter(is_staff=True))
            dispositivos = FCMDevice.objects.all().filter(user__in=usuarios)
            dispositivos.send_message(
                title="Se ha ingresado una nueva solicitud de contacto!",
                body=f"{nombre_contacto} ha enviado una solicitud de contacto.",
                icon="/static/web/img/001-24-hours.png"
            )
        else:
            data["form"] = formulario
    return render(request, 'web/contacto.html',data)

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
            nombre_insumo = formulario.cleaned_data["nombre"]
            usuarios = list(User.objects.all())
            dispositivos = FCMDevice.objects.all().filter(user__in=usuarios)
            dispositivos.send_message(
                title="Se ha ingresado un nuevo insumo!",
                body=f"{nombre_insumo} ahora esta disponible como insumo.",
                icon="/static/web/img/001-24-hours.png"
            )
            
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

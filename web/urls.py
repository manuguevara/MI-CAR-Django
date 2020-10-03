from django.urls import path
from .views import home, galeria, insumos, misionvision, registro, ubicacion

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('insumos/', insumos, name="insumos"),
    path('misionvision/', misionvision, name="misionvision"),
    path('registro/', registro, name="registro"),
    path('ubicacion/', ubicacion, name="ubicacion"),
]

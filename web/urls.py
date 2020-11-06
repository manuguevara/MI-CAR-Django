from django.urls import path
from .views import home, galeria, misionvision, registro, ubicacion, agregar_insumo, listar_insumos, modificar_insumo, eliminar_insumo

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('misionvision/', misionvision, name="misionvision"),
    path('registro/', registro, name="registro"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('agregar-insumo/', agregar_insumo, name="agregar_insumo"),
    path('listar-insumos/', listar_insumos, name="listar_insumos"),
    path('modificar-insumo/<id>/', modificar_insumo, name="modificar_insumo"),
    path('eliminar-insumo/<id>/', eliminar_insumo, name="eliminar_insumo"),
]

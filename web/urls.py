from django.urls import path, include
from .views import home, galeria, misionvision, registro, ubicacion, \
agregar_insumo, listar_insumos, modificar_insumo, eliminar_insumo, InsumoViewset, error_facebook, save_token,contacto, ContactoViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('insumo',InsumoViewset)
router.register('contacto',ContactoViewset)
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
    path('solicitud-contacto', contacto, name="solicitud_contacto"),
    path('api/',include(router.urls)),
    path('error-facebook/', error_facebook, name="error_facebook"),
    path('save-token/', save_token, name="save_token"),
]

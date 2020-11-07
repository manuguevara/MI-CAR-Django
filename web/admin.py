from django.contrib import admin
from .models import Slider, Galeria, MisionVision, Insumo

# Register your models here.
class ImagenAdmin(admin.ModelAdmin):
    list_display = ["imagen"]
    search_fields = ["imagen"]
    list_per_page = 10

class MisionVisionAdmin(admin.ModelAdmin):
    list_display = ["texto1", "texto2", "imagen", "mision", "vision"]
    search_fields = ["texto1", "texto2", "imagen", "mision", "vision"]
    list_per_page = 10

class InsumoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","imagen","descripcion","stock"]
    search_fields = ["nombre","precio","imagen","descripcion","stock"]
    list_per_page = 10

admin.site.register(Slider, ImagenAdmin)
admin.site.register(Galeria, ImagenAdmin)
admin.site.register(MisionVision, MisionVisionAdmin)
admin.site.register(Insumo)


#Modificacion de titulos sitio administracion

admin.site.site_header = "Administración de MiCar"
admin.site.site_title = "MiCar"
admin.site.index_title = "Panel de administración"


from django.contrib import admin
from .models import Categoria
from .models import Servicio

class CategoriaAdmin(admin.ModelAdmin):
    list_display= ("nombre", "descripcion")
class ServicioAdmin(admin.ModelAdmin):
    list_display= ("nombre", "descripcion","direccion", "precio","id_Categoria")



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Servicio,ServicioAdmin)
from django.contrib import admin
from .models import Categoria
from .models import Servicio
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class CategoriaAdmin(admin.ModelAdmin):
    list_display= ("nombre", "descripcion")
class ServicioAdmin(admin.ModelAdmin):
    list_display= ("nombre", "descripcion","direccion", "precio","id_Categoria")

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Servicio,ServicioAdmin)
from django.contrib import admin
from .models import Categoria, Cliente, Administrador, Clientes_admin, Propiedades, Comprobante_Pago, Operacion, Mensajes, Servicio
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass


# tablas bd
class Cliente_admin(admin.ModelAdmin):
    list_display=('Nombre_Apellido','DNI','Tipo_cliente','id_cliente')
class Administrador_admin(admin.ModelAdmin):
    list_display=('Nombre_Apellido','Alias_admin')
class ClientesAdmin_admin(admin.ModelAdmin):
    list_display=('id_cliente','Tipo_cliente','Alias_admin' )
class Propiedades_admin(admin.ModelAdmin):
    list_display=('Tipo_propiedad', 'Precio_alquiler', 'Alias_admin', 'ID_propiedad')
class Operación_admin(admin.ModelAdmin):
    list_display=('Nro_operación','Tipo_operación','Fecha_inicio','ID_propiedad')
class Comprobante_admin(admin.ModelAdmin):
    list_display=('Nro_comprobante','Descripción_operación')
class Mensajes_admin(admin.ModelAdmin):
    list_display=('Nro_mensaje','Asunto')
class CategoriaAdmin(admin.ModelAdmin):
    list_display= ("nombre", "descripcion")
class ServicioAdmin(admin.ModelAdmin):
    list_display= ("nombre", "descripcion","direccion", "precio","id_Categoria")

admin.site.register(Cliente, Cliente_admin)
admin.site.register(Administrador, Administrador_admin)
admin.site.register(Clientes_admin, ClientesAdmin_admin)
admin.site.register(Propiedades, Propiedades_admin)
admin.site.register(Operacion, Operación_admin)
admin.site.register(Comprobante_Pago,Comprobante_admin)
admin.site.register(Mensajes,Mensajes_admin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Servicio,ServicioAdmin)


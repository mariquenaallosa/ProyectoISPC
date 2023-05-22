from django.db import models

# Create your models here.
#Tabla de Servicios y la tabla de Categorias
class Categoria(models.Model):
    id_Categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)
    descripcion = models.TextField(max_length=1000, blank=False)
    class Meta:
        db_table = "categoria"
        verbose_name = "categorias de servicios"
        verbose_name_plural = "Categorias"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    
class Servicio(models.Model):
    dni = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)
    descripcion = models.TextField(max_length=1000, blank=False)
    direccion = models.TextField(max_length=100, blank=False)
    precio = models.DecimalField(max_length=100,max_digits=10,blank=False, decimal_places=2)
    id_Categoria = models.ForeignKey(Categoria, to_field="id_Categoria" ,on_delete=models.CASCADE)
    class Meta:
        db_table = "Servicio"
        verbose_name = "servicios a realizar"
        verbose_name_plural = "servicios"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
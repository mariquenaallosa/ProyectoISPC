from django.db import models

#admin
class Admin (models.Model):
        self.alias = models.CharField(max_length=30)
        self.cbu = models.PositiveBigIntegerField()
        self.permisos = models.BinaryField()

def agregarPropiedad(self):
        print('El admin: ' + self.alias + ' puede agregar propiedades')

pruebaAdmin = Admin('lobo.oeste', 154666512488784, True)

pruebaAdmin.agregarPropiedad()
#########Falta adaptar resto de clases a django
#clientes-inquilinos

import mysql.connector

class Conectar():

    def __init__(self) -> None:    
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'contraseñabd',
                db = 'bd_administración_bienes_raices'
            )

        except mysql.connector.Error as descipcionError:
            print('¡No se conectó!', descipcionError)

    def traerInquilinos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = 'SELECT * FROM db_admin_bienes_raices.cliente WHERE Tipo_cliente LIKE "Inquilino";'

                cursor.execute(sentenciaSQL)
                resultadoInquilinos = cursor.fetchall()
                self.conexion.commit()
                self.conexion.close()

                return resultadoInquilinos

            except:
                print('No se pudo conectar a la base de datos')

#cliente
class Cliente:

    def __init__(self, tipoCliente, fechaAlta, nYA, dni, email, telefono, domicilio):
        self.tipoCliente = tipoCliente
        self.fechaAlta = fechaAlta
        self.nYA = nYA
        self.dni = dni
        self.email = email
        self.telefono = telefono
        self.domicilio = domicilio

    def cargaComprobante(self):
        print('Usuario: ' + self.nYA +
              ' DNI: ' + str(self.dni) +
              ' pagó el monto pactado y este es su comprobante')

    def esInquilino(self):
        if self.tipoCliente == 'inquilino':
            return print('Si, es Inquilino')


miCliente1 = Cliente('comprador', '31-10-2022', 'Nico lopez', 45666888, 'dumbish@hotmail.com', 154888666, 'esquina 0')

miCliente2 = Cliente('inquilino', '1-11-2022', 'jose rojo', 42222665, 'bichssnka@hotmail.com', 154888996, 'los andes 123')


miCliente1.cargaComprobante()

miCliente2.esInquilino()

# El ultimo método solo es de prueba

#ejemplo CRUD
class Conectar():

    def __init__(self) -> None:    
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'contraseñabd',
                db = 'bd_administración_bienes_raices'
            )

        except mysql.connector.Error as descipcionError:
            print('¡No se conectó!', descipcionError)

# Primera operación del CRUD: INSERT

    def insertarValor(self, ID_Cliente, E_mail, Tipo_Cliente, Fecha_alta, NyA, DNI, Telefono, Domicilio):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = 'INSERT INTO Cliente (ID_Cliente, E_mail, Tipo_Cliente, Fecha_alta, NyA, DNI, Telefono, Domicilio) VALUES (1, "prueba@hotmail.com", "Inquilino", DATE("2022-11-03"), "Locomotora Castro", 45586752, 485962355, "los sauces");'
                data = (ID_Cliente, E_mail, Tipo_Cliente, Fecha_alta, NyA, DNI, Telefono, Domicilio)

                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print('No se pudo conectar a la base de datos')

# Segunda Operación CRUD: READ

    def traerTablaCliente(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = 'SELECT * FROM db_admin_bienes_raices.cliente;'

                cursor.execute(sentenciaSQL)
                resultadoTablaCliente = cursor.fetchall()
                self.conexion.close()

                return resultadoTablaCliente

            except:
                print('No se pudo conectar a la base de datos')

# Tercera operación CRUD: UPDATE


    def actualizarRegistro(self, ID_Cliente):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = 'UPDATE Cliente SET NyA = "Jorge Pintos" WHERE ID_Cliente = 1;'
                data = (ID_Cliente)

                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print('No se pudo conectar a la base de datos')



# Cuarta operación CRUD: DELETE

    def EliminarRegistro(self, ID_Cliente):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM Cliente WHERE ID_Cliente = 1;"
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
                self.conexion.close()
            
            except:
                print('No se pudo conectar a la base de datos')

#Mensajes
class Mensajes:

    def __init__(self, nro_mensaje, asunto, fecha, descripcion_msj):
        self.nro_mensaje = nro_mensaje
        self.asunto = asunto
        self.fecha = fecha
        self.descripcion_msj = descripcion_msj

    def nuevoMsj(self):
        print('fecha ' + self.fecha +
         ' Asunto: ' + self.asunto + 
         ' Mensaje: ' + self.descripcion_msj)


pruebaMsj = Mensajes(1, 'Cañeria rota', '08/11/2022', 'Necesito una solución')

pruebaMsj.nuevoMsj()

#Operaciones
class Operación:

    def __init__(self, nro_operacion, tipo_operacion, fecha_inicio, fecha_fin, comision, motivo_pago, total_expensas, pago_total):
        self.nro_operacion = nro_operacion
        self.tipo_operacion = tipo_operacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.comision = comision
        self.motivo_pago = motivo_pago
        self.total_expensas = total_expensas
        self.pago_total = pago_total

    def crearComprobante(self):
        print('Comprobante de operación nro: ' + str(self.nro_operacion) +
        ' Se realizó un pago total de: ' + str(self.pago_total) +
        ' con fecha: ' + self.fecha_fin +
        ' la comisión del administrador es de: ' + str(self.comision))


pruebaOperación = Operación(1, 'alquiler', '01-11-2022', '08-11-2022', 12000, 'pago alquiler', 20000, 72000)


pruebaOperación.crearComprobante()

#Propiedades
class Propiedades:

    def __init__(self, tipo_propiedad, ubicacion, superficie, cant_ambientes, limite_ocupantes, permite_mascotas, apto_credito, tasación, precio_alquiler):
        self.tipo_propiedad = tipo_propiedad
        self.ubicacion = ubicacion
        self.superficie = superficie
        self.cant_ambientes = cant_ambientes
        self.limite_ocupantes = limite_ocupantes
        self.permite_mascotas = permite_mascotas
        self.apto_credito = apto_credito
        self.tasación = tasación
        self.precio_alquiler = precio_alquiler

    def comprarPrecio(self):
        print('Si quieres comprar esta propiedad el precio es de: ' + str(self.tasación))

    def alquilarPrecio(self):
        print('Si quieres alquilar esta propiedad el precio por mes es de: ' + str(self.precio_alquiler))


pruebaPropiedad = Propiedades('Departamento', 'Cordoba, Vila Carlos Paz', 1200, 5, 10, True, False, 60000000, 50000)


pruebaPropiedad.comprarPrecio()
pruebaPropiedad.alquilarPrecio()
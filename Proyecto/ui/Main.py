from datetime import datetime
from platform import system

from proyectoBD.dominio.DireccionVivienda import DireccionVivienda
from proyectoBD.dominio.Inquilino import Inquilino
from proyectoBD.dominio.Alquiler import Alquiler
from proyectoBD.dominio.AgenciaInmobiliaria import AgenciaInmobiliaria
from proyectoBD.dominio.Propietario import Propietario
from proyectoBD.dominio.Vivienda import Vivienda
import os

def Agencia(id):
    if not AgenciaInmobiliaria.mostrarAgencias(id):
        return
    salidaAgencia = False
    while(salidaAgencia == False):
        os.system('cls')
        print("Opciones:")
        print("1) Crear Alquiler")
        print("2) Mostrar Propiedades")
        print("3) Corroborar si Alquiler es renovación")
        print("4) Salir")

        resp = input()
        match resp:
            case "1":
                os.system('cls')
                id_alquiler = input("Ingrese el ID del alquiler: ")
                vivienda = input("Ingrese el ID vivienda: ")

                dni_inquilino = input("Ingrese el DNI del inquilino: ")
                telefono = input("Ingrese el telefono: ")
                fecha_nacimiento = datetime.strptime(input("Ingrese la fecha de nacimiento (YYYY-MM-DD): "),"%Y-%m-%d").date()
                nombre = input("Ingrese el nombre del inquilino: ")
                apellido_paterno = input("Ingrese el apellido paterno: ")
                apellido_materno = input("Ingrese el apellido materno: ")

                inquilino = Inquilino(dni_inquilino, telefono, fecha_nacimiento, nombre, apellido_paterno, apellido_materno)
                Alquiler.registrarInquilino(inquilino)

                alquiler_padre = input("Ingrese ID del alquiler que se renueva, en caso contrario presionar Enter: ")
                if alquiler_padre == "":
                    alquiler_padre = None
                else:
                    alquiler_padre = int(alquiler_padre)
                fecha_firma = datetime.today().date()
                fecha_inicio = datetime.strptime(input("Ingrese el fecha inicio (YYYY-MM-DD): "), "%Y-%m-%d").date()
                fecha_fin = datetime.strptime(input("Ingrese el fecha fin (YYYY-MM-DD): "), "%Y-%m-%d").date()
                importe = input("Ingrese el importe del alquiler: ")
                fianza = input("Ingrese fianza del alquiler: ")

                alquiler = Alquiler(id_alquiler,vivienda, dni_inquilino, alquiler_padre, fecha_firma, fecha_inicio, fecha_fin, importe, fianza)
                Alquiler.regitraralquiler(alquiler)
            case "2":
                os.system('cls')
                AgenciaInmobiliaria.listarVivienda()

            case "3":
                datos = Alquiler.consultarTodo()
                for d1 in datos:
                    print()
                    for d2 in d1:
                        print(d2, end=", ")
                print()
                id_reno = input("Ingrese el ID del Alquiler: ")
                print(Alquiler.consultar_renovacion(id_reno))
            case "4":
                salidaAgencia = True
            case _:
                print("ERROR: Valor inválido\n")


def PropietarioUi(dni):
    if not Propietario.mostrarPropietario(dni):
        return
    salidaPropietario = False
    while(salidaPropietario == False):
        os.system('cls')
        print("Opciones:")
        print("1) Registrar vivienda")
        print("2) Mostrar viviendas")
        print("3) Salir")

        resp = input()
        match resp:
            case "1":
                os.system('cls')
                id_vivienda = input("Ingrese el ID del vivienda: ")
                descripcion = input("Ingrese la descripcion del vivienda: ")

                calle = input("Ingrese calle de la vivienda: ")
                numero = input("Ingrese numero de la vivienda: ")
                cp = input("Ingrese CP de la vivienda: ")
                poblacion = input("Ingrese Poblacion de la vivienda: ")
                direccion = DireccionVivienda(calle, numero, cp, poblacion)
                agencia = input("Ingrese el id de la agencia: ")

                vivienda = Vivienda(id_vivienda, descripcion, direccion, agencia, dni)
                Propietario.registrarVivienda(vivienda)
            case "2":
                os.system('cls')
                viviendas = Propietario.vervivienda(dni)
                if viviendas:
                    for v in viviendas:
                        print(v)
                else:
                    print("No hay viviendas registradas.")
            case "3":
                salidaPropietario = True
            case _:
                print("ERROR: Valor inválido\n")

def InquilinoUI(dni):
    if not Inquilino.mostrarInquilino(dni):
        return

    salidaInquilino = False
    while(salidaInquilino == False):
        os.system('cls')
        print("Opciones:")
        print("1) Ver alquiler")
        print("2) Salir")

        resp = input()
        match resp:
            case "1":
                os.system('cls')
                alquileres = Alquiler.consultarPorDni(dni)
                if alquileres:
                    registro = alquileres[0]
                    for campo in registro:
                        print(campo, end=", ")
                else:
                    print("No se encontró ningún alquiler.")
                print()
            case "2":
                salidaInquilino = True




salida = False
while(salida == False):
    os.system('cls')
    print("Tipo de usuario:")
    print("1) Agencia Inmobiliaria")
    print("2) Propietario")
    print("3) Inquilino")
    print("4) Salir")

    respuesta = input()
    match respuesta:
        case "1":
            os.system('cls')
            print("Ingresar ID")
            idAg = input()
            Agencia(idAg)
        case "2":
            os.system('cls')
            print("Ingresar DNI")
            dniPr = input()
            PropietarioUi(dniPr)
        case "3":
            os.system('cls')
            print("Ingresar DNI")
            dniIq = input()
            InquilinoUI(dniIq)
        case "4":
            salida = True
        case _:
            print("ERROR: Valor invalido\n")

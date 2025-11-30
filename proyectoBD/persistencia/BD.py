import mariadb
import sys

#Credenciales de la BD
userBD = "root"
passBD = "78927182"
hostBD = "localhost"
portBD = 3306
nameBD = "inmobiliaria"


def conectar():
    try:
        conexion = mariadb.connect(
            user=userBD,
            password=passBD,
            host=hostBD,
            port=portBD,
            database=nameBD
        )
        return  conexion
    except mariadb.Error as e:
        print(f"Error al establecer conexion: {e}")
        sys.exit(1)

def consulta(instruccion, parametros): #Debe usarse para comandos que devuelven datos
    conexion = conectar() #Regresa un objeto de tipo conexion
    BD = conexion.cursor() #Regresa un objeto cursor para manipular la BD
    BD.execute(instruccion, parametros) #Ejecuta el comando recibido
    datos = BD.fetchall() #Convierte el resultado en una lista de tuplas
    cerrar(BD, conexion) #Cierra la conexion abierta
    return datos #Regresa los datos obtenidos


def actualizacion(instruccion, datos): #Debe usarse para comandos que modifican la base de datos
    conexion = conectar() #Abre y regresa objeto de tipo conexion
    BD = conexion.cursor() #Crea y regresa un objeto cursos para manipular la BD
    BD.execute(instruccion, datos) #Ejecuta comandos
    conexion.commit() #Refleja el cambio en la base de datos
    cerrar(BD, conexion) #Cierra la conexion con la BD

def cerrar(BD, conexion):
    BD.close()
    conexion.close()


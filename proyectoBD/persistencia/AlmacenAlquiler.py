from dataclasses import dataclass #https://docs.python.org/es/3.10/library/dataclasses.html
from datetime import date
import mariadb
from proyectoBD.dominio.Alquiler import Alquiler
import proyectoBD.persistencia.BD as BD

@dataclass
class AlmacenAlquiler:

    @staticmethod
    def guardar(alquiler : Alquiler) -> bool:
        datos = (
            alquiler.id,
            alquiler.fecha_firma,
            alquiler.fecha_inicio,
            alquiler.fecha_final,
            alquiler.importe_mensual,
            alquiler.fianza,
            alquiler.vivienda,
            alquiler.inquilino,
            alquiler.alquiler_padre,
        )

        instruccion = "INSERT INTO alquiler (ID_ALQUILER, FECHA_FIRMA, FECHA_INICIO, FECHA_FIN, IMPORTE_MENSUAL, FIANZA, ID_VIVIENDA, DNI_INQUILINO, ID_ALQUILER_PADRE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        try:
            return BD.actualizacion(instruccion, datos)
        except mariadb.Error as e:
            print(f"Error al agregar alquiler: {e}")
            return False

    @staticmethod
    def consultarPorID_alquiler(id_alquier : int) -> bool:
        instruccion = "SELECT * FROM alquiler WHERE ID_ALQUILER = ?"
        try:
            return BD.consulta(instruccion,(id_alquier,))
        except mariadb.Error as e:
            print(f"Error al mostrar alquiler: {e   }")
            return False

    @staticmethod
    def consultarPorDNI(dni: str) -> bool:
        instruccion = "SELECT * FROM alquiler WHERE DNI_INQUILINO = ?"
        try:
            return BD.consulta(instruccion, (dni,))
        except mariadb.Error as e:
            print(f"Error al mostrar alquiler: {e}")
            return False

    @staticmethod
    def consultarTodosAlquilers() -> bool:
        instruccion = "SELECT * FROM alquiler"
        try:
            return BD.consulta(instruccion, ())
        except mariadb.Error as e:
            print(f"Error al mostrar alquileres: {e}")
            return False

    def consultar_renovacion(id_alquiler : int) -> bool:
        instruccion = "SELECT ID_ALQUILER, IF(ID_ALQUILER_PADRE IS NULL, 'No', 'Si') AS HAY_RENOVACION FROM alquiler WHERE ID_ALQUILER = ?;"
        try:
            return BD.consulta(instruccion, (id_alquiler,))
        except mariadb.Error as e:
            print(f"Error al realizar la consulta: {e}")
            return False

from _pydatetime import date
from dataclasses import dataclass
from proyectoBD.dominio.Inquilino import Inquilino
import mariadb
import proyectoBD.persistencia.BD as BD

@dataclass
class Alquiler:
    id: int
    vivienda:  int
    inquilino: str
    alquiler_padre: int
    fecha_firma: date
    fecha_inicio: date
    fecha_final: date
    importe_mensual: float
    fianza:float

    @staticmethod
    def registrarInquilino(inquilino: Inquilino):
        Inquilino.registrarInquilino(inquilino)

    @staticmethod
    def Duracion(id):
        instruccion = "SELECT * FROM v_alquiler_duracion WHERE ID_ALQUILER = ?;"
        datos= (id)
        try:
            return BD.actualizacion(instruccion, datos)

        except mariadb.Error as e:
            print(f"Error al calcular duracion: {e}")
            return False
    @staticmethod
    def regitraralquiler(alquiler):
        from proyectoBD.persistencia.AlmacenAlquiler import AlmacenAlquiler
        AlmacenAlquiler.guardar(alquiler)

    @staticmethod
    def consultarPorDni(dni: str):
        from proyectoBD.persistencia.AlmacenAlquiler import AlmacenAlquiler
        return AlmacenAlquiler.consultarPorDNI(dni)

    @staticmethod
    def consultarPorId(id: int):
        from proyectoBD.persistencia.AlmacenAlquiler import AlmacenAlquiler
        return AlmacenAlquiler.consultarPorID_alquiler(id)

    @staticmethod
    def consultarTodo():
        from proyectoBD.persistencia.AlmacenAlquiler import AlmacenAlquiler
        return AlmacenAlquiler.consultarTodosAlquilers()

    @staticmethod
    def consultar_renovacion(id_alquiler: int):
        from proyectoBD.persistencia.AlmacenAlquiler import AlmacenAlquiler
        return AlmacenAlquiler.consultar_renovacion(id_alquiler)


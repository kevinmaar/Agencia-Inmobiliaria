from dataclasses import dataclass #https://docs.python.org/es/3.10/library/dataclasses.html
from datetime import date
import mariadb

from proyectoBD.dominio.Inquilino import Inquilino
import proyectoBD.persistencia.BD as BD


@dataclass
class AlmacenInquilino:

    @staticmethod
    def guardar(inquilino: Inquilino) -> bool:
        instruccion = "INSERT INTO inquilino(DNI_INQUILINO, TELEFONO, FECHA_NACIMIENTO, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO) VALUES (?,?,?,?,?,?)"
        datos = (
            inquilino.id,
            inquilino.telefono,
            inquilino.fecha_nacimiento,
            inquilino.nombre,
            inquilino.apellido_paterno,
            inquilino.apellido_materno
        )
        try:
            BD.actualizacion(instruccion, datos)
            return True
        except mariadb.Error as e:
            print(f"Error al guardar inquilino: {e}")
            return False

    @staticmethod
    def consultar(id:  str):
        instruccion="SELECT * FROM inquilino WHERE DNI_INQUILINO = ?"
        try:
            return BD.consulta(instruccion, (id,))
        except mariadb.Error as e:
            print(f"Error al consultar inquilino: {e}")
            return False
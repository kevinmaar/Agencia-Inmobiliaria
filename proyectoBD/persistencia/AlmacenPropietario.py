from dataclasses import dataclass #https://docs.python.org/es/3.10/library/dataclasses.html
from datetime import date
import mariadb
from proyectoBD.dominio.Propietario import Propietario
import proyectoBD.persistencia.BD as BD

@dataclass
class AlmacenPropietario:

    @staticmethod
    def guardar(propietario: Propietario) -> bool:
        datosPropietario = (
            propietario.id,
            propietario.telefono,
            propietario.email,
            propietario.nombre,
            propietario.apellido_paterno,
            propietario.apellido_materno
        )
        datosDireccion = (
            propietario.id,
            propietario.direccion.calle,
            propietario.direccion.numero,
            propietario.direccion.cp,
            propietario.direccion.poblacion,
        )
        instruccionPropietario = "INSERT INTO propietario (DNI_PROPIETARIO, TELEFONO, EMAIL, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO) VALUES (?, ?, ?, ?, ?, ? )"
        instruccionDireccion = "INSERT INTO direccion_propietario (DNI_PROPIETARIO, CALLE, NUMERO, CP, POBLACION) VALUES (?, ?, ?, ?, ?)"

        try:
            BD.actualizacion(instruccionPropietario, datosPropietario)
            try:
                BD.actualizacion(instruccionDireccion, datosDireccion)
                return True
            except mariadb.Error as b:
                print(f"Error al agregar la direccion del propietario: {b}")
                return False
        except mariadb.Error as e:
            print(f"Error al agregar propietario: {e}")
            return False

    @staticmethod
    def consultar(id_propietario: str) -> bool:

        consulta = "SELECT * FROM propietario INNER JOIN direccion_propietario ON propietario.DNI_PROPIETARIO = direccion_propietario.DNI_PROPIETARIO WHERE propietario.DNI_PROPIETARIO = ?"
        try:
            return BD.consulta(consulta, (id_propietario,))
        except mariadb.Error as e:
            print(f"Error al consultar propietario: {e}")
            return False

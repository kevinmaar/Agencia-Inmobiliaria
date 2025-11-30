from dataclasses import dataclass #https://docs.python.org/es/3.10/library/dataclasses.html

import mariadb
import proyectoBD.persistencia.BD as BD
from proyectoBD.dominio.DireccionVivienda import DireccionVivienda
from proyectoBD.dominio.Vivienda import Vivienda

@dataclass
class AlmacenVivienda():

    @staticmethod
    def guardar(vivienda: Vivienda) -> bool:
        datosVivienda = (
            vivienda.id,
            vivienda.descripcion,
            vivienda.agencia,
            vivienda.propietario
        )

        datosDireccion = (
            vivienda.id,
            vivienda.direccion.calle,
            vivienda.direccion.numero,
            vivienda.direccion.cp,
            vivienda.direccion.poblacion
        )
        instruccionVivienda = "INSERT INTO vivienda (ID_VIVIENDA, DESCRIPCION, ID_AGENCIA, DNI_PROPIETARIO) VALUES (?, ?, ?, ?)"
        instruccionDireccion = "INSERT INTO direccion_vivienda (ID_VIVIENDA, CALLE, NUMERO, CP, POBLACION) VALUES (?, ?, ?, ?, ?)"

        try:
            BD.actualizacion(instruccionVivienda, datosVivienda)
            try:
                BD.actualizacion(instruccionDireccion, datosDireccion)
                return True
            except mariadb.Error as b:
                print(f"Error al guardar la direccion de vivienda: {b}")
                return False
        except mariadb.Error as e:
            print(f"Error al agregar vivienda: {e}")
            return False

    @staticmethod
    def consultar() -> bool:
        instruccion = "SELECT * FROM vivienda INNER JOIN direccion_vivienda ON vivienda.ID_VIVIENDA = direccion_vivienda.ID_VIVIENDA"
        try:
            return BD.consulta(instruccion, ())
        except mariadb.Error as e:
            print(f"Error al consultar viviendas: {e}")
            return False

    @staticmethod
    def consultarConDireccion(direcc: DireccionVivienda) -> bool:
        instruccion = "SELECT * FROM vivienda INNER JOIN direccion_vivienda on vivienda.ID_VIVIENDA = direccion_vivienda.ID_VIVIENDA WHERE CALLE = ? AND NUMERO = ? AND CP = ? AND POBLACION = ? "
        datos = (
            direcc.calle,
            direcc.numero,
            direcc.cp,
            direcc.poblacion
        )
        try:
            return BD.consulta(instruccion, datos)
        except mariadb.Error as e:
            print(f"Error al mostrar: {e}")
            return False

    @staticmethod
    def consultarConPropietario(id: str) -> bool:
        instruccion = "SELECT vivienda.ID_VIVIENDA, vivienda.DESCRIPCION, vivienda.ID_AGENCIA, direccion_vivienda.CALLE, direccion_vivienda.NUMERO, direccion_vivienda.CP  FROM vivienda INNER JOIN direccion_vivienda ON direccion_vivienda.ID_VIVIENDA = vivienda.ID_VIVIENDA INNER JOIN propietario on vivienda.DNI_PROPIETARIO = propietario.DNI_PROPIETARIO WHERE propietario.DNI_PROPIETARIO = ?"
        datos = (id,)
        try:
            return BD.consulta(instruccion, datos)
        except mariadb.Error as e:
            print(f"Error al mostrar: {e}")
            return False


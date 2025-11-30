from dataclasses import dataclass #https://docs.python.org/es/3.10/library/dataclasses.html
import mariadb
import proyectoBD.persistencia.BD as BD
from proyectoBD.dominio.AgenciaInmobiliaria import AgenciaInmobiliaria

@dataclass

class AlmacenAgencia:

    @staticmethod
    def guardar(agencia: AgenciaInmobiliaria) -> bool:
        datosAgencia = (
            agencia.id_agencia,
            agencia.rfc,
            agencia.telefono,
        )
        datosDireccionAgencia = (
            agencia.id_agencia,
            agencia.direccion.calle,
            agencia.direccion.numero,
            agencia.direccion.cp,
            agencia.direccion.poblacion
        )
        instruccionInmobiliaria = "INSERT INTO agencia_inmobiliaria(ID_AGENCIA, RFC, TELEFONO) VALUES (?, ?, ?)"
        instruccionDireccion = "INSERT INTO direccion_agencia(ID_AGENCIA, CALLE, NUMERO, CP, POBLACION) VALUES (?, ?, ?, ?, ?)"
        try:
            BD.actualizacion(instruccionInmobiliaria, datosAgencia)
            try:
                BD.actualizacion(instruccionDireccion, datosDireccionAgencia)
                return True
            except mariadb.Error as b:
                print(f"Error al agregar la direccion de la agencia: {b}")
                return False
        except mariadb.Error as e:
            print(f"Error al agregar inmobiliaria: {e}")
            return False

    @staticmethod
    def consultar(id: int) -> bool:
        instruccion = "SELECT * FROM agencia_inmobiliaria INNER JOIN direccion_agencia ON agencia_inmobiliaria.ID_AGENCIA = direccion_agencia.ID_AGENCIA  WHERE agencia_inmobiliaria.ID_AGENCIA = ?"
        try:
            return BD.consulta(instruccion, (id,))
        except mariadb.Error as e:
            print(f"Error al consultar inmobiliaria: {e}")
            return False

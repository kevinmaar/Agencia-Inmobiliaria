from dataclasses import dataclass #https://docs.python.org/es/3.10/library/dataclasses.html
import mariadb
import proyectoBD.persistencia.BD as BD
from proyectoBD.dominio.AgenciaInmobiliaria import AgenciaInmobiliaria
@dataclass
class AlmacenAgencia:

    @staticmethod
    def guardar(agencia: AgenciaInmobiliaria):
        print(123)

    @staticmethod
    def consultar(id: str):
        print(123)

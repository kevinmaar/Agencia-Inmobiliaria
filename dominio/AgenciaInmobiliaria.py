from dataclasses import dataclass
from proyectoBD.dominio.DireccionAgencia import DireccionAgencia
from proyectoBD.dominio.DireccionVivienda import Direccionvivienda
import mariadb
import proyectoBD.persistencia.BD as BD

@dataclass
class AgenciaInmobiliaria:
    id_agencia: int
    rfc: str
    telefono: str
    direccion: DireccionAgencia
    
    def mostrarPropiedad(direccion: Direccionvivienda) -> bool:
        instruccion = "SELECT * FROM vivienda JOIN direccion_vivienda on vivienda.ID_VIVIENDA = direccion_vivienda.ID_VIVIENDA WHERE  = ?"


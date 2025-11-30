from dataclasses import dataclass

from proyectoBD.dominio.AgenciaInmobiliaria import AgenciaInmobiliaria
from proyectoBD.dominio.DireccionVivienda import Direccionvivienda
from proyectoBD.dominio.Propietario import Propietario
@dataclass
class Vivienda:
    id: int
    descripcion: str
    direccion: Direccionvivienda
    agencia : AgenciaInmobiliaria
    propietario: Propietario

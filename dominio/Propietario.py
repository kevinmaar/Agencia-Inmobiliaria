from dataclasses import dataclass

from proyectoBD.dominio.DireccionPropietario import DireccionPropietario


@dataclass
class Propietario:
    id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    telefono: str
    email: str
    direccion: DireccionPropietario
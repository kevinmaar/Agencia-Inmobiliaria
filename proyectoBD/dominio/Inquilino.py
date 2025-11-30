from dataclasses import dataclass
from datetime import date

@dataclass
class Inquilino:
    id: str #ERROR, este dato debe ser string ya que la BD lo marca como varchar, antes era int
    telefono: str
    fecha_nacimiento: date
    nombre: str
    apellido_paterno: str
    apellido_materno: str

    @staticmethod
    def mostrarInquilino(id):
        from proyectoBD.persistencia.AlmacenInquilino import AlmacenInquilino
        return (AlmacenInquilino.consultar(id))
    @staticmethod
    def registrarInquilino(inquilino):
        from proyectoBD.persistencia.AlmacenInquilino import AlmacenInquilino
        AlmacenInquilino.guardar(inquilino)


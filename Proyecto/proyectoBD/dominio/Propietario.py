from dataclasses import dataclass
from proyectoBD.dominio.DireccionPropietario import DireccionPropietario
from proyectoBD.dominio.Vivienda import Vivienda


@dataclass
class Propietario:
    id: str
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    telefono: str
    email: str
    direccion: DireccionPropietario

    @staticmethod
    def vervivienda(id):
        from proyectoBD.dominio.Vivienda import Vivienda
        return Vivienda.motrarViviendaPropietario(id)

    @staticmethod
    def registrarPropietario(propietario):
        from proyectoBD.persistencia.AlmacenPropietario import AlmacenPropietario
        AlmacenPropietario.guardar(propietario)

    def mostrarPropietario(id):
        from proyectoBD.persistencia.AlmacenPropietario import AlmacenPropietario
        return AlmacenPropietario.consultar(id)

    def registrarVivienda(vivienda: Vivienda):
        from proyectoBD.dominio.Vivienda import Vivienda
        Vivienda.registrarVivienda(vivienda)
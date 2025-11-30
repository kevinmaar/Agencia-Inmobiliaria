from dataclasses import dataclass
from proyectoBD.dominio.DireccionVivienda import DireccionVivienda


@dataclass
class Vivienda:
    id: int
    descripcion: str
    direccion: DireccionVivienda
    agencia : int
    propietario: str

    @staticmethod
    def mostrarViviendaDireccion(direccion: DireccionVivienda):
        from proyectoBD.persistencia.AlmacenVivienda import AlmacenVivienda
        return AlmacenVivienda.consultarConDireccion(direccion)

    @staticmethod
    def motrarViviendaPropietario(id_propietario):
        from proyectoBD.persistencia.AlmacenVivienda import AlmacenVivienda
        return AlmacenVivienda.consultarConPropietario(id_propietario)

    @staticmethod
    def listar():
        from proyectoBD.persistencia.AlmacenVivienda import AlmacenVivienda
        BD = AlmacenVivienda.consultar()
        for row in BD:
            print(row)

    @staticmethod
    def registrarVivienda(vivienda):
        from proyectoBD.persistencia.AlmacenVivienda import AlmacenVivienda
        AlmacenVivienda.guardar(vivienda)

from dataclasses import dataclass
from proyectoBD.dominio.DireccionAgencia import DireccionAgencia
from proyectoBD.dominio.Vivienda import Vivienda


@dataclass
class AgenciaInmobiliaria:
    id_agencia: int
    rfc: str
    telefono: str
    direccion: DireccionAgencia

    @staticmethod
    def mostrarAgencias(id_agencia):
        from proyectoBD.persistencia.AlmacenAgencia import AlmacenAgencia
        return AlmacenAgencia.consultar(id_agencia)

    @staticmethod
    def registrarAgencia(agencia):
        from proyectoBD.persistencia.AlmacenAgencia import AlmacenAgencia
        AlmacenAgencia.guardar(agencia)

    @staticmethod
    def listarVivienda():
        from proyectoBD.dominio.Vivienda import Vivienda
        Vivienda.listar()

    def registrarVivienda(vivienda: Vivienda):
        from proyectoBD.dominio.Vivienda import Vivienda
        Vivienda.registrarVivienda(vivienda)
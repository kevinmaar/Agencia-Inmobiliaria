from _pydatetime import date
from dataclasses import dataclass
from proyectoBD.dominio.Inquilino import Inquilino
from proyectoBD.dominio.Vivienda import Vivienda
@dataclass
class Alquiler:
    id: int
    vivienda: Vivienda
    inquilino: Inquilino
    alquiler_padre: int
    fecha_firma: date
    fecha_inicio: date
    importe_mensual: float
    fianza:float
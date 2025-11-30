from dataclasses import dataclass

@dataclass
class DireccionVivienda:
    calle: str
    numero: str
    cp: str
    poblacion: str

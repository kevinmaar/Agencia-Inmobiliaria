from proyectoBD.dominio.Inquilino import Inquilino
from datetime import datetime

# Crear objeto Inquilino
fecha = datetime.strptime("07/04/06", "%d/%m/%y").date()
inq1 = Inquilino("123","2711532277", fecha,"Juan","Antonio","Ramirez")

# Registrar y mostrar
Inquilino.registrarInquilino(inq1)
Inquilino.mostrarInquilino("123")

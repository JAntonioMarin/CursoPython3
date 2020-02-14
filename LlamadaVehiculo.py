from Vehiculo import Vehiculo
from Vehiculo import Electrico

moto = Vehiculo("toyota")
moto.encender()
moto.estado()
moto.apagar()
moto.estado()

tesla = Electrico("Tesla")
tesla.estadoBateria()
tesla.cargar()
tesla.estadoBateria()
tesla.descargar()

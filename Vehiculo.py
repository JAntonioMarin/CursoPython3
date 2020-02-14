
class Vehiculo:

    def __init__(self, CAR):
        print("Objeto vehiculo creado")
        self.__CAR = CAR
        self.__encendido = False # __ pone los atributos en privado e igual con las funciones.

    def __del__(self):
        print("Destruye el objeto", self.__CAR)

    def encender(self):
        self.__encendido = True

    def apagar(self):
        self.__encendido = False

    def estado(self):
        if self.__encendido:
            print("El coche está encendido")
        else:
            print("El coche está apagado")

#Herencia

class Electrico(Vehiculo):

    def __init__(self, CAR):
        super().__init__(CAR)
        self.__bateria = 0
    def cargar(self):
        self.__bateria = 100
    def descargar(self):
        self.__bateria = 0
    def estadoBateria(self):
        print(f"Bateria {self.__bateria} %")

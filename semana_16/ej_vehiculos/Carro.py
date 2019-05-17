from semana_16.ej_vehiculos.Vehiculo import Vehiculo

class Carro(Vehiculo):

    def __init__(self, placa, color):
        super().__init__(4, placa, color)

    def mover(self, distancia):
        if self.encendido:
            return f'Moviendose {distancia}'
        else:
            raise Exception('El carro no está encendido')

    def reversa(self):
        super().reversa()

    def encender(self):
        return super().encender()

    def frenar(self):
        super().frenar()
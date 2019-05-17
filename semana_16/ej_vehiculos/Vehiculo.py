class Vehiculo:

    n_ruedas = 0
    placa = ''
    color = ''
    encendido = False


    def __init__(self, n_ruedas, placa, color):
        self.n_ruedas = n_ruedas
        self.placa = placa
        self.color = color
        self.encendido = False

    def mover(self, distancia):
        pass

    def reversa(self):
        pass

    def encender(self):
        """
        Enciende el vehiculo si este se encuentra apagado de lo contrario lo apaga

        :return: El estado del vehiculo
        """
        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True
        return self.encendido

    def frenar(self):
        pass
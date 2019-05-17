from unittest import TestCase
from semana_16.ej_vehiculos.Vehiculo import Vehiculo

class TestVehiculo(TestCase):

    def test_encender(self):
        #Valido la inicialización del vehiculo
        print('--- Inicia prueba de creación del vehiculo ---')
        dado = Vehiculo(4, 'BAD-768', 'Plata')
        espero = False
        recibo = dado.encendido
        self.assertEqual(espero, recibo)

        # Valida que se encienda el vehiculo
        print('--- Inicia prueba de encendido del vehiculo ---')
        espero = True
        recibo = dado.encender()
        self.assertEqual(espero, recibo)

        # Valida que se apague el vehiculo
        print('--- Inicia prueba de Apagado del vehiculo ---')
        espero = False
        recibo = dado.encender()
        self.assertEqual(espero, recibo)



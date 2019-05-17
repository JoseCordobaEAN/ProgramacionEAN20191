from unittest import TestCase
from semana_16.ej_vehiculos.Carro import Carro


class TestCarro(TestCase):
    def test_mover(self):
        mi_carro = Carro('SYJ-123', 'Rosa')
        print(f'--- inicia la prueba de conducción para el carro {mi_carro} ---')
        # Probar que se mueve si esta encedido
        espero = 'Moviendose 10'
        mi_carro.encender()
        resultado = mi_carro.mover(10)
        self.assertEqual(espero, resultado)

        #self.fail()

    def test_reversa(self):
        self.fail()

    def test_encender(self):
        self.fail()

    def test_frenar(self):
        self.fail()

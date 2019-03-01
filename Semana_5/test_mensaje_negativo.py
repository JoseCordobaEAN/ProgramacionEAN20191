from unittest import TestCase
import Semana_5.ejemplos_if_2 as f

class TestMensaje_negativo(TestCase):

    def test_mensaje_negativo(self):
        self.assertEqual(f.mensaje_negativo(-653), 'El numero es negativo')
        self.assertEqual(f.mensaje_negativo(653), 'El numero es positivo')

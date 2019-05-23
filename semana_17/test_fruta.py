from unittest import TestCase
from Fruta import Fruta

class TestFruta(TestCase):
    def test_pelar(self):
        # Probar con nuevas frutas
        dado = Fruta('banano', 10)
        espero = True
        real = dado.pelar()

        self.assertEqual(real, espero)

        # Probar cuando la fruta ya esta pelada
        self.assertRaises(ValueError, dado.pelar)


    def test_cortar(self):
        dado = Fruta('papaya', 1000)
        espero = 130

        real = dado.cortar(1)
        self.assertEqual(espero, real)

    def test_licuar(self):
        self.fail()

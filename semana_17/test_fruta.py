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
        self.fail()

    def test_licuar(self):
        self.fail()

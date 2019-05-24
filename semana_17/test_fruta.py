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

        # Validar que la fruta este pelada para cortar
        self.assertRaises(ValueError, dado.cortar,1)

        # Valida si la papaya produce la cantidad esperada
        dado.pelar()
        espero = 130
        real = dado.cortar(1)
        self.assertEqual(espero, real)

    def test_licuar(self):
        dado = Fruta('piña', 1000)

        # Validar que la fruta este pelada para cortar
        self.assertRaises(ValueError, dado.licuar, 1)

        # Valida si la piña produce la cantidad esperada
        dado.pelar()
        espero = 3000
        real = dado.licuar(2)
        self.assertEqual(espero, real)

import unittest
import Semana_4.funciones2 as f

class pruebas(unittest.TestCase):

    def test_es_vocal(self):
        self.assertTrue(f.es_vocal('a'),'Probando con a')
        self.assertTrue(f.es_vocal('e'))
        self.assertTrue(f.es_vocal('i'))
        self.assertTrue(f.es_vocal('o'))
        self.assertTrue(f.es_vocal('u'))
        self.assertFalse(f.es_vocal('G'))
        self.assertFalse(f.es_vocal('aooo'))


if __name__ == 'main':
    unittest.main()
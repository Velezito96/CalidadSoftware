import unittest
from Calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(sumar(0, 0), 0)
        self.assertEqual(sumar(100, 200), 300)

    def test_sumar_error(self):
        with self.assertRaises(ValueError):
            sumar('a', 2)
        with self.assertRaises(ValueError):
            sumar(2, 'b')
        with self.assertRaises(ValueError):
            sumar('a', 'b')

    def test_restar(self):
        self.assertEqual(restar(100, 50), 50)

    def test_restar_error(self):
        with self.assertRaises(ValueError):
            restar('a', 2)
        with self.assertRaises(ValueError):
            restar(2, 'b')
        with self.assertRaises(ValueError):
            restar('a', 'b')

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(-1, -1), 1)
        self.assertEqual(multiplicar(0, 1), 0)
        self.assertEqual(multiplicar(5, 5), 25)

    def test_multiplicar_error(self):
        with self.assertRaises(ValueError):
            multiplicar('a', 2)
        with self.assertRaises(ValueError):
            multiplicar(2, 'b')
        with self.assertRaises(ValueError):
            multiplicar('a', 'b')

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(0, 1), 0)

    def test_dividir_error(self):
        with self.assertRaises(ValueError):
            dividir(4, 0)
        with self.assertRaises(ValueError):
            dividir('a', 2)
        with self.assertRaises(ValueError):
            dividir(4, 'b')
        with self.assertRaises(ValueError):
            dividir('a', 'b')
        with self.assertRaises(ValueError):
            dividir(-10, -2)

if __name__ == "__main__":
    unittest.main()

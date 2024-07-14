import unittest
from unittest.mock import patch
import random

# Supongamos que tu código está en un archivo llamado sopa_letras.py
from SopaLetras import es_suficiente_tamano, generar_matriz, es_posible_colocar, colocar_palabra, rellenar_matriz, \
    encontrar_mejor_posicion


class TestSopaLetras(unittest.TestCase):

    def test_es_suficiente_tamano(self):
        self.assertTrue(es_suficiente_tamano(10, ["PALABRA", "LETRA"]))
        self.assertFalse(es_suficiente_tamano(5, ["PALABRA", "LETRA"]))

    def test_generar_matriz(self):
        matriz = generar_matriz(3)
        self.assertEqual(len(matriz), 3)
        self.assertEqual(len(matriz[0]), 3)
        self.assertTrue(all(cell == ' ' for row in matriz for cell in row))

    def test_es_posible_colocar_horizontal(self):
        matriz = generar_matriz(5)
        self.assertTrue(es_posible_colocar(matriz, "TEST", "horizontal", 0, 0))
        self.assertFalse(es_posible_colocar(matriz, "TEST", "horizontal", 0, 2))

    def test_es_posible_colocar_vertical(self):
        matriz = generar_matriz(5)
        self.assertTrue(es_posible_colocar(matriz, "TEST", "vertical", 0, 0))
        self.assertFalse(es_posible_colocar(matriz, "TEST", "vertical", 2, 0))

    def test_es_posible_colocar_diagonal_positiva(self):
        matriz = generar_matriz(5)
        self.assertTrue(es_posible_colocar(matriz, "TEST", "diagonal_positiva", 3, 0))
        self.assertFalse(es_posible_colocar(matriz, "TEST", "diagonal_positiva", 0, 0))

    def test_es_posible_colocar_diagonal_negativa(self):
        matriz = generar_matriz(5)
        self.assertTrue(es_posible_colocar(matriz, "TEST", "diagonal_negativa", 0, 0))
        self.assertFalse(es_posible_colocar(matriz, "TEST", "diagonal_negativa", 3, 0))

    def test_colocar_palabra_horizontal(self):
        matriz = generar_matriz(5)
        colocar_palabra(matriz, "TEST", "horizontal", 0, 0)
        self.assertEqual(matriz[0][:4], list("TEST"))

    def test_colocar_palabra_vertical(self):
        matriz = generar_matriz(5)
        colocar_palabra(matriz, "TEST", "vertical", 0, 0)
        self.assertEqual([matriz[i][0] for i in range(4)], list("TEST"))

    def test_colocar_palabra_diagonal_positiva(self):
        matriz = generar_matriz(5)
        colocar_palabra(matriz, "TEST", "diagonal_positiva", 3, 0)
        self.assertEqual([matriz[3 - i][i] for i in range(4)], list("TEST"))

    def test_colocar_palabra_diagonal_negativa(self):
        matriz = generar_matriz(5)
        colocar_palabra(matriz, "TEST", "diagonal_negativa", 0, 0)
        self.assertEqual([matriz[i][i] for i in range(4)], list("TEST"))

    @patch('random.choice')
    def test_rellenar_matriz(self, mock_choice):
        mock_choice.side_effect = lambda x: 'X'
        matriz = generar_matriz(5)
        rellenar_matriz(matriz)
        self.assertTrue(all(cell == 'X' for row in matriz for cell in row))

    @patch('random.sample')
    def test_encontrar_mejor_posicion(self, mock_sample):
        mock_sample.side_effect = [list(range(10)), list(range(10))]
        matriz = generar_matriz(10)
        posicion = encontrar_mejor_posicion(matriz, "TEST", 0)
        self.assertIsNotNone(posicion)


if __name__ == "__main__":
    unittest.main()

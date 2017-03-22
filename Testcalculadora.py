from unittest import TestCase

from Calculadora import Calculadora
class TestCalculadora(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"cadena vacia")

    def test_sumar_unacadena(self):
        self.assertEqual(Calculadora().sumar("1"),1,"un numero")

    def test_sumar_unacadenaUnNumero(self):
        self.assertEqual(Calculadora().sumar("1"),1,"un numero")
        self.assertEqual(Calculadora().sumar("2"), 2, "un numero")
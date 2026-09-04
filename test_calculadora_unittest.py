import unittest
from calculadora import soma


class TestSoma(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 6)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)


if __name__ == '__main__':
    unittest.main()

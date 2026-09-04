from calculadora import soma


def test_soma_positivos():
    assert soma(2, 3) == 6


def test_soma_negativos():
    assert soma(-1, -1) == -2

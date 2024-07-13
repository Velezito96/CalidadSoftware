import pytest
from prueba_1_codigo import sumar, restar, multiplicar, dividir


@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300)
])
def test_sumar(a, b, resultado):
    assert sumar(a, b) == resultado


@pytest.mark.parametrize("a, b", [
    ('a', 2),
    (2, 'b'),
    ('a', 'b')
])
def test_sumar_error(a, b):
    with pytest.raises(ValueError):
        sumar(a, b)


@pytest.mark.parametrize("a, b, resultado", [

    (100, 50, 50)
])
def test_restar(a, b, resultado):
    assert restar(a, b) == resultado


@pytest.mark.parametrize("a, b", [
    ('a', 2),
    (2, 'b'),
    ('a', 'b')
])
def test_restar_error(a, b):
    with pytest.raises(ValueError):
        restar(a, b)


@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 6),
    (-1, -1, 1),
    (0, 1, 0),
    (5, 5, 25)
])
def test_multiplicar(a, b, resultado):
    assert multiplicar(a, b) == resultado


@pytest.mark.parametrize("a, b", [
    ('a', 2),
    (2, 'b'),
    ('a', 'b')
])
def test_multiplicar_error(a, b):
    with pytest.raises(ValueError):
        multiplicar(a, b)


@pytest.mark.parametrize("a, b, resultado", [
    (6, 3, 2),
    (10, 2, 5),
    (0, 1, 0)
])
def test_dividir(a, b, resultado):
    assert dividir(a, b) == resultado


@pytest.mark.parametrize("a, b", [
    (4, 0),
    ('a', 2),
    (4, 'b'),
    ('a', 'b'),
    (-10, -2)

])

def test_dividir_error(a, b):
    with pytest.raises(ValueError):
        dividir(a, b)

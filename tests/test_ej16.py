from src.ej16 import encontrar_numero_mayor

def test_encontrar_numero_mayor():
    assert encontrar_numero_mayor([1, 2, 4, 3]) == 4
    assert encontrar_numero_mayor([19, 23, 100, 99]) == 100
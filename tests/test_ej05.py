from src.ej05 import calcular_capital

def test_calcular_capital():
    assert calcular_capital(100, 10) == 110.00
    assert calcular_capital(1000, 10) == 1100.00

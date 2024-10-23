from src.ej22 import contar_pares_e_impares

def test_contar_pares_e_impares():
    assert contar_pares_e_impares(123) == (1, 2)
    assert contar_pares_e_impares(246) == (3, 0)
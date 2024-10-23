from src.ej20 import comparar_letras

def test_comparar_letras():
    assert comparar_letras("a", "a") == True
    assert comparar_letras("a", "d") == False
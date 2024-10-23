from src.ej18 import convertir_en_lista
from src.ej18 import sumar_lista_numeros

def test_convertir_en_lista():
    assert convertir_en_lista("123") == ["1", "2", "3"]

def test_sumar_lista_numeros():
    assert sumar_lista_numeros(0, ["1", "2"]) == 3
    assert sumar_lista_numeros(0, ["1", "2", "3"]) == 6
from src.ej25 import calcular_longitud_palabras
from src.ej25 import encontrar_palabra_mas_larga

def test_calcular_longitud_palabras():
    assert calcular_longitud_palabras(["hola", "loco"]) == [4, 4] 
    assert calcular_longitud_palabras(["hola", "buenas"]) == [4, 6] 

def test_encontrar_palabra_mas_larga():
    assert encontrar_palabra_mas_larga(["hola", "buenas"], [4, 6] ) == "buenas"
    assert encontrar_palabra_mas_larga(["holaaaa", "buenas"], [7, 6] ) == "holaaaa"
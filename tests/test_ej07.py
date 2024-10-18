from src.ej07 import multiplicar
from src.ej07 import generar_linea_mensaje

def test_multiplicar():
    assert multiplicar(2,2) == 4

def test_generar_linea_mensaje():
    assert generar_linea_mensaje(1, 10, "",10) == "- 1 x 10 = 10\n"
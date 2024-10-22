from src.ej08 import generar_triangulo

def test_generar_triangulo():
    assert generar_triangulo(1) == "1 \n"
    assert generar_triangulo(2) == "1 \n3 1 \n"
    assert generar_triangulo(3) == "1 \n3 1 \n5 3 1 \n"
from src.ej06 import generar_triangulo

def test_generar_triangulo():
    assert generar_triangulo(1) == " * \n"
    assert generar_triangulo(2) == " * \n *  * \n"
    assert generar_triangulo(3) == " * \n *  * \n *  *  * \n"
from src.ej11 import mostrar_cadena_invertida

def test_mostrar_cadena_invertida():
    assert mostrar_cadena_invertida("a") == "a\n"
    assert mostrar_cadena_invertida("al") == "l\na\n"
    assert mostrar_cadena_invertida("aloh") == "h\no\nl\na\n"
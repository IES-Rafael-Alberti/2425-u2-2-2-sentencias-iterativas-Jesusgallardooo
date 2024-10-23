from src.ej12 import contar_coincidencias

def test_contar_coincidencias():
    assert contar_coincidencias("hola", "a") == 1
    assert contar_coincidencias("holaaaa", "a") == 4
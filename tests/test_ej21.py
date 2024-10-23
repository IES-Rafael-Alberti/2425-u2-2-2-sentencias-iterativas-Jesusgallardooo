from src.ej21 import descontar_10_prcnt
from src.ej21 import generar_mensaje

def test_calcular_10_prcnt():
    assert descontar_10_prcnt(100) == 90
    assert descontar_10_prcnt(1000) == 900

def test_generar_mensaje():
    assert generar_mensaje(1000) == "La suma total a pagar es --> 900.0€."
    assert generar_mensaje(10000) == "La suma total a pagar es --> 9000.0€."
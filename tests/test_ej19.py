from src.ej19 import generar_menu
from src.ej19 import comprobar_opcion

def test_generar_menu():
    assert generar_menu() == "\n\t 1- comenzar programa\n\t 2- comenzar programa\n\t 3- finalizar programa\n"
    
def test_comprobar_opcion():
    assert comprobar_opcion(3) == "\n"
    assert comprobar_opcion(1) == "\n\tDale a tu cuerpo alegría Macarena, \n\tQue tu cuerpo es pa darle alegría y cosa buena, \n\tDale a tu cuerpo alegría, Macarena,\n\tHey Macarena, aaay! \n"
    assert comprobar_opcion(2) == "\n\tDale a tu cuerpo alegría Macarena, \n\tQue tu cuerpo es pa darle alegría y cosa buena, \n\tDale a tu cuerpo alegría, Macarena,\n\tHey Macarena, aaay! \n"
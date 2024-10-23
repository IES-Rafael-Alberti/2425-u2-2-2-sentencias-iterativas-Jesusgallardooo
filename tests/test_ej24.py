from src.ej24 import comprobar_primo
from src.ej24 import contar_primos

def test_comprobar_primo():
    assert comprobar_primo(2) == True
    assert comprobar_primo(1) == False
    assert comprobar_primo(4) == False
    assert comprobar_primo(61) == True
    
def test_contar_primos():
    assert contar_primos(1, 0) == 0  
    assert contar_primos(3, 1) == 2
    assert contar_primos(5, 2) == 3
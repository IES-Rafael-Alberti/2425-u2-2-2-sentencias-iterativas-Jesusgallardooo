from src.ej10 import comprobar_primo

def test_comprobar_primo():
    assert comprobar_primo(2) == True
    assert comprobar_primo(1) == False
    assert comprobar_primo(4) == False
    assert comprobar_primo(61) == True
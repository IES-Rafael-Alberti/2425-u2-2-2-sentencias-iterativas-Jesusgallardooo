from src.ej09 import comprobar_password

def test_comprobar_password():
    assert comprobar_password("hoasda") == False
    assert comprobar_password("contraseña") == True
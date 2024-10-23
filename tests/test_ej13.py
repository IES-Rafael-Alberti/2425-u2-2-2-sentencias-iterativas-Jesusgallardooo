from src.ej13 import escuchar_usuario

def test_escuchar_usuario():
    assert escuchar_usuario("") == True
    assert escuchar_usuario("sdjfnsng") == True
    assert escuchar_usuario("salir") == False
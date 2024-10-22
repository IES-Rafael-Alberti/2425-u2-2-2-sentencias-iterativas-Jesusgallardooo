from src.ej01 import mostrar_cadena_10_veces

def test_mostrar_cadena_10_veces():
    assert mostrar_cadena_10_veces("a") == (
        "\n1. a\n" +
        "\n2. a\n" +
        "\n3. a\n" +
        "\n4. a\n" +
        "\n5. a\n" +
        "\n6. a\n" +
        "\n7. a\n" +
        "\n8. a\n" +
        "\n9. a\n" +
        "\n10. a\n" 
    )

def multiplicar(numero, multiplicador):
    resultado = numero * multiplicador
    return resultado

def salida(mensaje):
    print(mensaje)

def generar_mensaje():
    mensaje = ""

    for numero in range(1, 11):
        multiplicador = 1  # reinicia el multiplicador
        while multiplicador <= 10:
            resultado = multiplicar(numero, multiplicador)
            mensaje = generar_linea_mensaje(numero, multiplicador, mensaje, resultado)
            multiplicador += 1
        mensaje += "\n---\n\n"  

    return mensaje

def generar_linea_mensaje(numero, multiplicador, mensaje, resultado):
    mensaje = mensaje + "- " + str(numero) + " x " + str(multiplicador) + " = " + str(resultado) + "\n"
    return mensaje

def main():
    # Procesamiento
    mensaje = generar_mensaje()
    # Salida
    salida(mensaje)

if __name__ == "__main__":
    main()

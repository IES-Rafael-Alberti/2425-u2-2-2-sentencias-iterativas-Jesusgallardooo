# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def salida(loQueSea):
    print(loQueSea)

def generar_mensaje(contarLetras):
    mensaje = "Numero de coincidencias: " + str(contarLetras)
    return mensaje

def contar_coincidencias(frase, letraSeleccionada):
    
    contarLetras = 0
    
    for letra in frase:
        if letra == letraSeleccionada:
            contarLetras += 1
            
    return contarLetras

def entrada():
    frase = input("Introduzca una frase --> ")
    letraSeleccionada = input("Introduzca una letra --> ")
    return frase,letraSeleccionada

def main():
    
    # Entrada
    frase, letraSeleccionada = entrada()

    # Procesamiento
    contarLetras = contar_coincidencias(frase, letraSeleccionada)
    
    mensaje = generar_mensaje(contarLetras)
    
    # Salida
    salida(mensaje)


if __name__ == "__main__":
    
    main()
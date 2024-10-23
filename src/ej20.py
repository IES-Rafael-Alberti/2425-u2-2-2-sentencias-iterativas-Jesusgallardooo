#  Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, 
# comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y 
# continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def main():
    
    # Entrada
    frase, letraSeleccionada = entrada()
    frase = list(frase)
    
    # Procesamiento
    contarLetras = 0
    posicion = 1
    mensaje = ""

    while contarLetras == 0:
        
        for letra in frase:
            if comparar_letras(letraSeleccionada, letra):
                contarLetras += 1
                mensaje += " \t\t Coincidencia encontrada en la posicion --> " + str(posicion) + "\n"
                #break
            else:
                mensaje += "Coincidencia no encontrada en la posicion " + str(posicion) + "\n"
            
            posicion += 1

    # Salida
    salida(mensaje)

def comparar_letras(letraSeleccionada, letra):
    return letra == letraSeleccionada

def salida(mensaje):
    print(mensaje)

def entrada():
    frase = input("Introduzca una frase --> ")
    letra = input("Introduzca una letra --> ")
    return frase, letra

if __name__ == "__main__":
    main()
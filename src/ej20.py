#  Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, 
# comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y 
# continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def comparar_letras(letraSeleccionada, letra):
    return letra == letraSeleccionada

def salida(mensaje):
    print(mensaje)

def entrada():
    frase = input("Introduzca una frase --> ")
    letra = input("Introduzca una letra --> ")
    return frase, letra

def encontrar_coincidencia(frase, letraSeleccionada):
    
    contarLetras = 0
    posicion = 0
    mensaje = ""

    while contarLetras == 0:
        
        if comparar_letras(letraSeleccionada, frase[posicion]):
            contarLetras += 1
            mensaje += " \t\t Coincidencia encontrada en la posicion --> " + str(posicion) + "\n"
        else:
            mensaje += "Coincidencia no encontrada en la posicion " + str(posicion) + "\n"

        posicion += 1
        
    return mensaje

def main():
    
    # Entrada
    frase, letraSeleccionada = entrada()
    frase = list(frase)
    
    # Procesamiento
    while frase == "" or letraSeleccionada == "":
        print("No puedes dejar valores en blanco.")
        frase, letraSeleccionada = entrada()
    
    mensaje = encontrar_coincidencia(frase, letraSeleccionada)

    # Salida
    salida(mensaje)

if __name__ == "__main__":
    main()
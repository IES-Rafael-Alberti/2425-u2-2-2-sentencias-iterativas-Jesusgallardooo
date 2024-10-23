# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) 
# y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

def main():
    
    # Entrada
    palabras = entrada()
    
    #Procesamiento
    numeroDePalabras = len(palabras)
    
    longitudPalabras = calcular_longitud_palabras(palabras)
    
    palabraMasLarga = encontrar_palabra_mas_larga(palabras, longitudPalabras)
    
    mensaje = " La frase tiene " + str(numeroDePalabras)+ " palabra/s" + "\n\n la palabra mas larga es --> << " + palabraMasLarga + " >>."
    
    # Salida
    salida(mensaje)

def encontrar_palabra_mas_larga(palabras, longitudPalabras):
    indicePalabraMasLarga = longitudPalabras.index(max(longitudPalabras))
    palabraMasLarga = palabras[indicePalabraMasLarga]
    return palabraMasLarga

def salida(loQueSea):
    print (loQueSea)

def entrada():
    frase = input("Introduzca una frase --> ")
    palabras = frase.split(" ")
    return palabras

def calcular_longitud_palabras(palabras):
    
    longitudPalabras = []
    
    for i in range(len(palabras)):
        longitud = len(palabras[i])
        longitudPalabras.append(longitud)
        
    return longitudPalabras

if __name__ == "__main__":
    
    main()
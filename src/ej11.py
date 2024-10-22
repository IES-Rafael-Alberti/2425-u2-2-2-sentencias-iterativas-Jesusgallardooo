#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def salida(loQueSea):
    print(loQueSea)

def entrada():
    palabra = input("Introduzca una palabra --> ")
    return palabra

def mostrar_cadena_invertida(palabra):
    
    mensaje = ""
    
    for letra in reversed(palabra):
        mensaje += letra + "\n"
        
    return mensaje

def main():
    
    # Entrada
    palabra = entrada()
    
    # Procesamiento
    mensaje = mostrar_cadena_invertida(palabra)
    
    # Salida
    salida(mensaje)



if __name__ == "__main__":
    main()
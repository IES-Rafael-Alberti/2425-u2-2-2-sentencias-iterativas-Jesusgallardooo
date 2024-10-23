#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

def entrada():
    entrada = input("Introduzca un numero entero --> ")
    numero = validar_entrada(entrada)

    # Verifica si la entrada es válida
    while numero is None:
        entrada = input("Introduzca un numero entero --> ")
        numero = validar_entrada(entrada)
        
    return numero

def validar_entrada(numero):
    
    '''
    recibe:
        un numero.
        
    devuelve:
        - si es entero:
            > numero
        - si no es entero:
            > None
    '''
    
    try:
        numero = int(numero)  
        if numero != 0 :
            return numero
        else:
            return numero
    except ValueError:
        print("Entrada no válida. Debe introducir un número entero.")
        return None  

def salida(loQueSea):
    print(loQueSea)

def main():
    
    # Entrada
    numero = entrada()
    
    # Procesamiento
    suma = 0

    if numero == 0:
        mensaje = "fin del programa."
    else:
        while numero != 0:
            suma += numero
            numero = entrada()
            
        mensaje = "La suma de todos los numeros equivale a --> " + str(suma)
    
    # Salida
    salida(mensaje)



if __name__ == "__main__":
    
    main()
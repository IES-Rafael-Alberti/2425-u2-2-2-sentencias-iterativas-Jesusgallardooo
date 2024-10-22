def entrada():
    entrada = input("Introduzca un número entero positivo (0 para terminar) --> ")
    numero = validar_entrada(entrada)

    # Verifica si la entrada es válida
    while numero is None:
        entrada = input("Introduzca un número entero positivo (0 para terminar) --> ")
        numero = validar_entrada(entrada)
        
    return numero

def validar_entrada(numero):
    '''
    Recibe:
        Un número como cadena de texto.

    Devuelve:
        - Si es un entero positivo o 0: el número.
        - Si no es válido: None.
    '''
    
    try:
        numero = int(numero)
        if numero >= 0:
            return numero
        else:
            print("La entrada debe ser un número entero positivo.")
            return None
    except ValueError:
        print("Entrada no válida. Debe introducir un número entero positivo o 0.")
        return None  

def encontrar_numero_mayor(numeros):
    numeroMayor = max(numeros)
    return numeroMayor

def salida(loQueSea):
    print(loQueSea)
    
def main():

    # Entrada 
    numero = entrada()
    numeros = []
    
    # Procesamiento
    while numero != 0:
        numeros.append(numero)
        numero = entrada()  
    
    if numeros:  
        numeroMayor = encontrar_numero_mayor(numeros)
        mensaje = "El número mayor es --> " + str(numeroMayor)
    else:
        mensaje = "No hay ningún numero positivo."
        
    # Salida
    salida(mensaje)


if __name__ == "__main__":
    main()

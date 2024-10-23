# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

def entrada():
    entrada = input("Introduzca un numero entero positivo --> ")
    numero = validar_entrada(entrada)

    # Verifica si la entrada es válida
    while numero is None:
        entrada = input("Introduzca un numero entero positivo --> ")
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
        if numero > 0:
            return numero  
        else:
            print("La entrada debe ser un número entero positivo.")
            return None  
    except ValueError:
        print("Entrada no válida. Debe introducir un número entero positivo.")
        return None  

def salida(loQueSea):
    print(loQueSea)

def sumar_lista_numeros(listaNumeros):
    
    suma = 0
    for i in range(len(listaNumeros)):
        suma += int(listaNumeros[i])
        
    return suma

def convertir_en_lista(numero):
    return list(numero)


def main():
    
    # Entrada
    numero = str(entrada())
    
    # Procesamiento
    listaNumeros = convertir_en_lista(numero)
    suma = sumar_lista_numeros(listaNumeros)
    
    # Salida
    salida(suma)

if __name__ == "__main__":
    main()
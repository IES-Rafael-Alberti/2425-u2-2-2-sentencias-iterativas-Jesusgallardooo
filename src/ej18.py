# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario 
# fueron números pares.

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
        if numero > 0 or numero == -1:
            return numero  
        else:
            print("La entrada debe ser un número entero positivo.")
            return None  
    except ValueError:
        print("Entrada no válida. Debe introducir un número entero positivo.")
        return None  

def salida(loQueSea):
    print(loQueSea)
    
def main():
    
    # Entrada
    numero = str(entrada())
    
    # Procesamiento
    
    suma = 0
    
    while numero != "-1":
        
        listaNumeros = convertir_en_lista(numero)
        
        suma = sumar_lista_numeros(suma, listaNumeros)
        
        numero = str(entrada())
        
    # Salida
    salida(suma)

def sumar_lista_numeros(suma, listaNumeros):
    for i in range(len(listaNumeros)):
        suma += int(listaNumeros[i])
    return suma

def convertir_en_lista(numero):
    return list(numero)
        
        
if __name__ == "__main__":
    main()
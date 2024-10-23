# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, 
# informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares 
# leídos en total.

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
    recibe:
        un número como cadena.
        
    devuelve:
        - si es entero positivo o 0:
            > número convertido a entero
        - si no es entero:
            > None
    '''
    try:
        numero = int(numero)  
        if numero >= 0:  # Aceptamos 0 para detener el programa
            return numero
        else:
            return None
    except ValueError:
        print("Entrada no válida. Debe introducir un número entero positivo.")
        return None  

def contar_pares_e_impares(numero):
    '''
    recibe:
        un número entero positivo.
    
    devuelve:
        - cantidad de dígitos pares e impares en el número.
    '''
    contadorPares = 0
    contadorImpares = 0
    
    digitos = list(str(numero))
    
    for i in digitos:
        if int(i) % 2 == 0:
            contadorPares += 1
        else:
            contadorImpares += 1
    
    return contadorPares, contadorImpares

def salida(totalPares, totalImpares):
    print("Total de dígitos pares leídos: " + str(totalPares))
    print("Total de dígitos impares leídos: " + str(totalImpares))


def main():
    
    # Entrada
    numero = entrada()
    
    totalPares = 0
    totalImpares = 0
    
    # Procesamiento
    while numero != 0:

        pares, impares = contar_pares_e_impares(numero)
        
        totalPares += pares
        totalImpares += impares
        
        numero = entrada()
    
    # Salida
    salida(totalPares, totalImpares)

if __name__ == "__main__":
    main()

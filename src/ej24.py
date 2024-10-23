# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

def entrada():
    entrada = input("Introduzca un número entero positivo mayor que 1 (0 para terminar) --> ")
    numero = validar_entrada(entrada)

    # Verifica si la entrada es válida
    while numero is None:
        entrada = input("Introduzca un número entero positivo mayor que 1 (0 para terminar) --> ")
        numero = validar_entrada(entrada)
        
    return numero

def validar_entrada(numero):
    '''
    recibe:
        un número como cadena.
        
    devuelve:
        - si es entero positivo > 1 o 0:
            > número convertido a entero
        - si no es entero o es 1 :
            > None
    '''
    try:
        numero = int(numero)  
        if numero > 1 or numero == 0:  # Aceptamos 0 para detener el programa
            return numero
        else:
            print("Entrada no válida. Debe introducir un número entero positivo distinto de 1.")
            return None
    except ValueError:
        print("Entrada no válida. Debe introducir un número entero positivo distinto de 1.")
        return None  

def salida(loQueSea):
    print(loQueSea)
    
def comprobar_primo(numero):
    
    iterador = 1
    contadorDivisores = 0
    primo = bool

    while iterador <= numero:
        if numero % iterador == 0:
            contadorDivisores = contadorDivisores + 1
        
        iterador = iterador + 1
    
    if contadorDivisores ==  2:
        primo = True
    else:
        primo = False
        
    return primo

def main():
    
    # Entrada
    numero = entrada()
    contadorPrimos = 0
    
    # Procesamiento
    while numero != 0:
        
        contadorPrimos = contar_primos(numero, contadorPrimos)
        
        numero = entrada()
    
    mensaje = " - Numeros primos --> " + str(contadorPrimos)
    
    # Salida
    salida(mensaje)

def contar_primos(numero, contadorPrimos):
    if comprobar_primo(numero):
        contadorPrimos += 1
    else:
        contadorPrimos = contadorPrimos
    return contadorPrimos

if __name__ == "__main__":
    main()
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

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

def salida(loQueSea):
    print(loQueSea)

def main():

    # Entrada
    numero = entrada()
    
    # Procesamiento
    if comprobar_primo(numero):
        mensaje = "ES PRIMO!!!"
    else:
        mensaje = "NO ES PRIMO..."
    
    # Salida
    salida(mensaje)
    
if __name__ == "__main__":
    main()
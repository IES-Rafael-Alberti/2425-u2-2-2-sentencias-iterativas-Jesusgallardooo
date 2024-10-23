#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def salida(mensaje):
    print(mensaje)

def cuenta_atras(numero):
    contador = int(numero)
    mensaje = ""

    while contador >= 0:
        mensaje = mensaje +  str(contador) + ", "
        contador -= 1
    
    mensaje = mensaje[:-2]  # Quitar la última coma y espacio

    return mensaje

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

def main():

    #Entrada
    numero = entrada()

    #Procesamiento
    mensaje = cuenta_atras(numero)
    
    #Salida
    salida(mensaje)

if __name__ == "__main__":
    main()
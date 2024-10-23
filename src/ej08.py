#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla un triángulo rectángulo como el de más abajo. 

'''
    1
    3 1
    5 3 1
    7 5 3 1
    9 7 5 3 1
'''
def entrada():
    entrada = input("Introduzca un número entero positivo (número de filas) --> ")
    numero = validar_entrada(entrada)

    # Verifica si la entrada es válida
    while numero is None:
        entrada = input("Introduzca un número entero positivo --> ")
        numero = validar_entrada(entrada)
        
    return numero

def validar_entrada(numero):
    '''
    Recibe:
        un número.
        
    Devuelve:
        - si es entero:
            > número
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

def generar_triangulo(filas):
    mensaje = ""
    
    for i in range(filas):  
        
        fila = ""  
        primerImpar = 1 + (i * 2)  # Calcular el primer impar en cada fila

        for _ in range(i + 1):
            
            fila += str(primerImpar) + " "
            primerImpar -= 2  
        
        mensaje += fila + "\n"  
    
    return mensaje

def main():
    
    # Entrada
    numeroFilas = entrada()

    # Procesamiento
    trianguloImpares = generar_triangulo(numeroFilas)
    
    # Salida
    salida(trianguloImpares)

if __name__ == "__main__":
    main()

#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
#de altura el número introducido. 

'''
*
* *
* * *
* * * *
* * * * *
'''

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

def generar_triangulo(numero):

    contador = 1
    triangulo = ""
    mensaje = ""

    while contador <= int(numero):
        triangulo = triangulo + ("* ")
        mensaje = mensaje + triangulo + "\n"
        contador += 1
        
    return mensaje

def salida(mensaje):
    print(mensaje)

def main():

    #Entrada
    numero = entrada()

    #Procesamiento
    mensaje = generar_triangulo(numero)

    #Salida 
    salida(mensaje)

if __name__ == "__main__":
    main()
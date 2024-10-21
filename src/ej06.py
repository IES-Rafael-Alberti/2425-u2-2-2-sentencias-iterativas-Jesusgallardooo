#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
#de altura el número introducido. 

'''
*
* *
* * *
* * * *
* * * * *
'''

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
    numero = input("Introduzca un numero entero positivo --> ")

    #Procesamiento
    mensaje = generar_triangulo(numero)

    #Salida 
    salida(mensaje)

if __name__ == "__main__":
    main()
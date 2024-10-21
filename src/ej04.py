#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def salida(mensaje):
    print(mensaje)

def cuenta_atras(numero):
    contador = int(numero)
    mensaje = ""

    while contador >= 0:
        mensaje = mensaje +  str(contador) + ", "
        contador -= 1
    return mensaje

def entrada():
    numero = input("Introduzca un numero entero positivo --> ")
    return numero

def main():

    #Entrada
    numero = entrada()

    #Procesamiento
    mensaje = cuenta_atras(numero)
    
    #Salida
    salida(mensaje)

if __name__ == "__main__":
    main()
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def main():

    #Entrada
    #Entrada
    numero = input("Introduzca un numero entero positivo --> ")

    #Procesamiento
    contador = int(numero)
    mensaje = ""

    while contador >= 0:
        
        mensaje = mensaje +  str(contador) + ", "
        contador -= 1
    
    solucion = print(mensaje)

    #Salida
    return solucion

if __name__ == "__main__":
    main()
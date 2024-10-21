#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese 
#número separados por comas.

def agrupar_impares(numero):
    contador = 1
    mensaje = ""

    while contador <= int(numero):
        if comprobar_impar(contador) and (contador != numero or contador != numero - 1):
            mensaje = mensaje +  str(contador) + ", "
        elif comprobar_impar(contador) and (contador == numero or contador == numero - 1):
            mensaje = mensaje +  str(contador) + ""
        else:
            mensaje = mensaje

        contador += 1
    return mensaje

def entrada():
    numero = input("Introduzca un numero entero positivo --> ")
    return numero

def salida(mensaje):
    print(mensaje)

def comprobar_impar(contador):
    return contador%2 != 0

def comprobar_impar(contador):
    return contador%2 != 0

def main():

    #Entrada
    numero = entrada()

    #Procesamiento
    mensaje = agrupar_impares(numero)

    #Salida
    salida(mensaje)

if __name__ == "__main__":
    main()
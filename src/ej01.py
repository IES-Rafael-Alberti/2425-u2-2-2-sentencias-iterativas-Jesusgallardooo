#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def entrada():
    palabra = input("Introduzca una palabra --> ")
    return palabra

def salida(mensaje):
    print(mensaje)

def mostrar_cadena_10_veces(palabra):
    contador = 1
    mensaje = ""

    while contador <= 10:
        mensaje = mensaje + "\n" + str(contador) + ". " +palabra + "\n"
        contador += 1
    return mensaje

def main():

    #Entrada
    palabra = entrada()

    #Procesamiento
    mensaje = mostrar_cadena_10_veces(palabra)
    
    #Salida
    salida(mensaje)




if __name__ == "__main__":

    main()
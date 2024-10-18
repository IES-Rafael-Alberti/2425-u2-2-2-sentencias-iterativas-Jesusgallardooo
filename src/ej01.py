#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def main():

    #Entrada
    palabra = input("Introduzca una palabra --> ")

    #Procesamiento
    contador = 1
    mensaje = ""

    while contador <= 10:
        mensaje = mensaje + "\n" + str(contador) + ". " +palabra + "\n"
        contador += 1
    

    #Salida
    print(mensaje)
    

if __name__ == "__main__":

    main()
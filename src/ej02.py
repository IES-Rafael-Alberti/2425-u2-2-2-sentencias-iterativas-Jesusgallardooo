#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def main():
    
    #Entrada
    edad = (input("Introduzca su edad --> "))

    while not edad.isdigit():
        print("Dato incorrecto.")
        edad = (input("Introduzca su edad --> "))


    #Procesamiento
    contador = 1
    mensaje = ""

    while contador <= int(edad):
        mensaje = mensaje + "\n" + str(contador)
        contador += 1
    
    solucion = print("Has cumplido " + mensaje + " años.")

    #Salida
    return solucion

if __name__ == "__main__":
    main()
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def salida(mensaje):
    print("Has cumplido " + mensaje + " años.")

def validar_entrada(edad):
    while not edad.isdigit():
        print("Dato incorrecto.")
        edad = (input("Introduzca su edad --> "))
    return edad

def entrada():
    edad = (input("Introduzca su edad --> "))
    return edad


def main():
    
    #Entrada
    edad = entrada()
    edad = validar_entrada(edad)

    #Procesamiento
    mensaje = calcular_anios_cumplidos(edad)

    #Salida
    salida(mensaje)

def calcular_anios_cumplidos(edad):
    contador = 1
    mensaje = ""

    while contador <= int(edad):
        mensaje = mensaje + "\n" + str(contador)
        contador += 1
    return mensaje

if __name__ == "__main__":
    main()
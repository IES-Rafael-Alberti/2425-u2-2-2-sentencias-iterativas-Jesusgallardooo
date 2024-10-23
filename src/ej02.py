#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def salida(mensaje):
    print("Has cumplido " + mensaje + " años.")

def entrada():
    entrada = input("Introduzca su edad --> ")
    edad = validar_entrada(entrada)

    # Verifica si la entrada es válida
    while edad is None:
        entrada = input("Introduzca su edad --> ")
        edad = validar_entrada(entrada)

    return edad

def validar_entrada(edad):
    '''
        recibe: edad -> int
        
        devuelve:
        
            edad > int si es un entero positivo
            None > si no es un entero positivo
            
    '''
    if edad.isdigit():  # Verificar si la entrada es un entero positivo 
        return int(edad)
    else:
        print("Dato incorrecto. Debe introducir un número entero positivo.")
        return None

def calcular_anios_cumplidos(edad):
    contador = 1
    mensaje = ""

    while contador <= int(edad):
        mensaje = mensaje + "\n" + str(contador)
        contador += 1
    return mensaje

def main():
    # Entrada
    edad = entrada()

    # Procesamiento
    mensaje = calcular_anios_cumplidos(edad)

    # Salida
    salida(mensaje)

if __name__ == "__main__":
    main()


#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.ç


def multiplicar(numero, multiplicador):
    resultado = numero * multiplicador
    return resultado

def main():

    #Entrada
    numero = 1
    multiplicador = 1
    mensaje = ""
    
    #Procesamiento
    while multiplicador <= 10:
        resultado = multiplicar(numero, multiplicador)
        mensaje = generar_linea_mensaje(numero, multiplicador, mensaje, resultado)
        multiplicador += 1

    solucion = print(mensaje)

    #Salida
    return solucion

def generar_linea_mensaje(numero, multiplicador, mensaje, resultado):
    mensaje = mensaje + "- " + str(numero) + " x " + str(multiplicador) + " = " + str(resultado) + "\n"
    return mensaje

if __name__ == "__main__":
    main()
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla 
#el capital obtenido en la inversión cada año que dura la inversión.

def generar_mensaje_por_anio(amount, interest, anios):
    contador = 1
    mensaje = ""

    while contador <= anios:    
        capital = calcular_capital(amount, interest)
        mensaje = mensaje + "\n- Capital obtenido en el año " + str(contador) + " --> " + str(capital)
        amount = capital
        contador += 1
        
    return mensaje

def entrada():

    amount = float(input("Introduzca una cantidad a invertir --> "))
    interest = float(input("Introduzca el interes porcentual anual --> "))
    anios = int(input("Introduzca el numero de años que quieres invertirlo --> "))

    return amount,interest,anios

def salida(mensaje):
    print(mensaje)

def calcular_capital(amount, interest):
    capital = amount * (1 + interest / 100)
    return round(capital, 2)

def main():

    #Entrada
    amount, interest, anios = entrada()

    #Procesamiento
    mensaje = generar_mensaje_por_anio(amount, interest, anios)
    
    #Salida
    salida(mensaje)

if __name__ == "__main__":
    main()
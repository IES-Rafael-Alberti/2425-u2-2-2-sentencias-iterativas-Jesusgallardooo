# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la 
# contraseña hasta que introduzca la contraseña correcta.

def salida(mensaje):
    print(mensaje)

def entrada():
    intento = input("Introduzca la contraseña --> ")
    return intento


def comprobar_password(intento):
    password = "contraseña"
    return intento == password

def main():
    
    #Entrada
    intento = entrada()
    mensaje = ""
    
    # Procesamiento
    while not comprobar_password(intento):
        print("Contraseña incorrecta, pruebe otra vez...")
        intento = input("Introduzca la contraseña --> ")
    
    mensaje = " Contraseña correcta !!!"
    
    # Salida
    salida(mensaje)


if __name__ == "__main__":
    main()
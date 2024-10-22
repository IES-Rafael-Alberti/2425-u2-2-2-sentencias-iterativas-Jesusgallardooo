# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def sonar_eco(eco):
    print(eco)

def entrada():
    vozUsuario = input("Di algo --> ")
    vozUsuario = vozUsuario.lower()
    return vozUsuario

def main():
    
    # Entrada
    vozUsuario = entrada()
    
    # Procesamiento
    eco = ""
    
    while escuchar_usuario(vozUsuario):
        
        eco = "\t<<" + vozUsuario + ">>" + "\n\t\t<<" + vozUsuario + ">>"
        # Salida
        sonar_eco(eco)
        
        vozUsuario = entrada()

def escuchar_usuario(vozUsuario):
    return vozUsuario != "salir"


if __name__ == "__main__":
    main()
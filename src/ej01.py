def entrada():
    try:
        palabra = input("Introduzca una palabra --> ")
        if not palabra:
            raise ValueError("No has introducido ninguna palabra.")  # Lanza una excepción si la entrada está vacía
        return palabra
    except ValueError as e:
        print("Error: " + str(e))
        return entrada()  # Solicita otra vez la entrada en caso de error

def salida(mensaje):
    print(mensaje)

def mostrar_cadena_10_veces(palabra):
    contador = 1
    mensaje = ""

    while contador <= 10:
        mensaje = mensaje + "\n" + str(contador) + ". " + palabra + "\n"
        contador += 1
    return mensaje

def main():
    
    # Entrada
    palabra = entrada()

    # Procesamiento
    mensaje = mostrar_cadena_10_veces(palabra)
    
    # Salida
    salida(mensaje)

if __name__ == "__main__":
    main()

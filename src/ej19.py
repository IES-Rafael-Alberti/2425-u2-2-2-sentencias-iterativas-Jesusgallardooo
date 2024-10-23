# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario 
# debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a 
# mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige 
# la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

def entrada(menu):
    entrada = input("Seleccione una opción --> ")
    numero = validar_entrada(entrada, menu)

    # Verifica si la entrada es válida
    while numero is None:
        entrada = input("Seleccione una opción --> ")
        numero = validar_entrada(entrada, menu)
        
    return numero

def validar_entrada(numero, menu):
    
    '''
    recibe:
        un numero.
        
    devuelve:
        - si es distinto de 1, 2 o 3:
            > numero
        - si no es ni 1 ni 2 ni 3:
            > None
    '''
    
    try:
        numero = int(numero)  
        if numero == 1 or numero == 2 or numero == 3:
            return numero  
        else:
            print(generar_menu())
            print("La entrada debe ser un número asignado a una opción.")
            return None  
    except ValueError:
        print(generar_menu())
        print("Entrada no válida. Debe introducir un número asignado a una opción.")
        return None  

def generar_menu():
    return "\n\t 1- comenzar programa\n\t 2- comenzar programa\n\t 3- finalizar programa\n"

def salida(loQueSea):
    print(loQueSea)

def main():
    
    # Menu
    menu = generar_menu()

    # Entrada
    opcion = entrada(menu)
    
    # Procesamiento
    texto = ""
    
    texto = comprobar_opcion(opcion)
    
    # Salida
    salida(texto)

def comprobar_opcion(opcion):
    if opcion == 1 or opcion == 2:
        texto = "\n\tDale a tu cuerpo alegría Macarena, \n\tQue tu cuerpo es pa darle alegría y cosa buena, \n\tDale a tu cuerpo alegría, Macarena,\n\tHey Macarena, aaay! \n"
    else:
        texto = "\n"
    return texto

if __name__ == "__main__":
    main()
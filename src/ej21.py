# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, 
# la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, 
# no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas 
# superan el total de $1000, se le debe aplicar un 10% de descuento.

def entrada():
    entrada = input("Introduzca los montos de compra --> ")
    numero = validar_entrada(entrada)

    # Verifica si la entrada es válida
    while numero is None:
        entrada = input("Introduzca los montos de compra --> ")
        numero = validar_entrada(entrada)
        
    return numero

def validar_entrada(numero):
    '''
    recibe:
        un numero.
        
    devuelve:
        - si es positivo:
            > numero float
        - si no es entero:
            > None
    '''
    
    try:
        numero = float(numero)  
        if numero > 0 or numero == 0:
            return numero  
        else:
            print("El monto debe ser positivo o, si quiere salir 0.")
            return None  
    except ValueError:
        print("Entrada no válida. Debe introducir un monto positivo.")
        return None 

def salida(loQueSea):
    print(loQueSea)

def main():
    
    # Entrada
    montos = entrada()
    importeTotal = 0
    
    # Procesamiento
    while montos != 0 :
        
        importeTotal += montos
        montos = entrada()
    
    mensaje = generar_mensaje(importeTotal)
    
    # Salida
    salida(mensaje)

def generar_mensaje(importeTotal):
    if importeTotal >= 1000:
        importeTotal = descontar_10_prcnt(importeTotal)
        mensaje = "La suma total a pagar es --> " + str(importeTotal) + "€."
    else:
        mensaje = "La suma total a pagar es --> " + str(importeTotal) + "€."
    return mensaje

def descontar_10_prcnt(importeTotal):
    importeTotal = importeTotal - (importeTotal * 0.1)
    return importeTotal

if __name__ == "__main__":
    main()
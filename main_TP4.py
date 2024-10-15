def menu():
    print("***** GESTION DE ENVIOS POR CORREO *****")
    print("1. Crear archivo binario de registros\n"
          "2. Cargar envio por teclado\n"
          "3. Mostrar todos los registros del archivo binario\n"
          "4. Mostrar todos los registros del archivo con cp igual a valor ingresado por teclado\n"
          "5. Buscar en el archivo, registro cuya direccion postal sea igual a la ingresada por teclado\n"
          "6. Determinar y mostrar la cantidad de envios de cada combinacion posible entre tipo de envio y forma de pago\n"
          "7. Mostrar la cantidad total de envios contados por cada tipo de envio posible y forma de pago posible\n"
          "8. Calcular promedio pagado y generar un arreglo de registros con todos los envios con importes mayores al promedio\n"
          "0. Salir")
    op = int(input("?: "))
    while op < 0 or op > 8:
        op = int(input("Por favor, ingrese una opción válida (0 para salir): "))
    return op



def main():
    envios = []
    arrSuma_Envios = []
    f_run_program = True
    control = None
    while f_run_program:
        op = menu()
        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            pass
        else:
            f_run_program = False



if __name__ == '__main__':
    main()
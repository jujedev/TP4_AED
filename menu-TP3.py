"""from envio-TP3 import *


def menu():
    envios = []
    tipo_control = None
    acumulado = None

    while True:
        print("\nMenú de opciones:")
        print("1. Crear arreglo desde archivo")
        print("2. Cargar envío por teclado")
        print("3. Mostrar registros")
        print("4. Buscar por dirección y tipo")
        print("5. Buscar por código postal y cambiar forma de pago")
        print("6. Contar envíos válidos por tipo")
        print("7. Calcular importe final acumulado por tipo")
        print("8. Determinar tipo de envío con mayor importe final")
        print("9. Calcular importe final promedio")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            envios = crear_arreglo_desde_archivo(envios)
            tipo_control = control("envios-tp3.txt")  
            print(f"Control: {tipo_control}")
        elif opcion == 2:
            cargar_envio_por_teclado(envios)
        elif opcion == 3:
            mostrar_registros(envios)
        elif opcion == 4:
            direccion = input("Ingrese la dirección: ").strip()
            tipo_envio = int(input("Ingrese el tipo de envío: "))
            buscar_por_direccion_y_tipo(envios, direccion, tipo_envio)
        elif opcion == 5:
            codigo_postal = input("Ingrese el código postal: ").strip()
            buscar_por_codigo_postal(envios, codigo_postal)
        elif opcion == 6:
            if tipo_control:
                contar_envios_por_tipo(envios, tipo_control)
            else:
                print("Debe cargar los envíos primero.")
        elif opcion == 7:
            if tipo_control:
                acumulado = importe_final_acumulado(envios, tipo_control)
            else:
                print("Debe cargar los envíos primero.")
        elif opcion == 8:
            if acumulado:
                tipo_mayor, monto_mayor, porcentaje_mayor = tipo_envio_mayor_importe(acumulado)
                if tipo_mayor is not None:
                    print(f"Tipo de envío con mayor importe: {tipo_mayor} - Importe: {monto_mayor} - Porcentaje: {porcentaje_mayor:.2f}%")
                else:
                    print("No hay envíos con importes acumulados.")
            else:
                print("Debe calcular el importe acumulado primero.")
        elif opcion == 9:
            if tipo_control:
                promedio_importe, menores_que_promedio = calcular_importe_promedio(envios, tipo_control)
                if promedio_importe is not None:
                    print(f"Importe promedio: {promedio_importe:.2f}")
                    print(f"Número de envíos con importe menor al promedio: {menores_que_promedio}")
                else:
                    print("No se pudo calcular el importe promedio.")
            else:
                print("Debe cargar los envíos primero.")
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# -------------------------------------------------------------------- #

if __name__ == "__main__":
    menu()
"""

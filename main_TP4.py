import math

from Envio import Envio
import os
import pickle

def menu():
    print("***** GESTION DE ENVIOS POR CORREO *****")
    print("1. Crear archivo binario de registros\n"
          "2. Cargar envio por teclado y agregarlo al final del archivo bin\n"
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


def cop_csv_to_bin(name_arch):
    texto = open('envios-tp4.csv', 'rt')
    arch = open(name_arch, "w+b")

    for linea in texto:
        pickle.dump(linea, arch)

    arch.close()


def punto1():
    name_arch = "datos.dat"

    if os.path.exists(name_arch):
        print(f"Advertencia, ya existe el archivo {name_arch} , desea sobrescribir")
        print("1. Cancelar\n2. Sobrescribir")
        op = int(input("?: "))
        while op < 1 or op > 2:
            op = int(input("Por favor, ingrese una opción válida: "))
        if op == 1:
            return
        cop_csv_to_bin(name_arch)
    else:
        cop_csv_to_bin(name_arch)


# Punto 2
def crear_envio():
    cp = input("Ingrese el Codigo Postal: ")
    df = input("Ingrese la dirección física: ")
    tp = int(input("Ingrese el tipo de envío: "))
    while tp < 0 or tp > 6:
        tp = int(input("Por favor, ingrese un valor entre 0 y 6: "))
    fp = int(input("Ingrese la forma de pago: "))
    while fp < 1 or fp > 2:
        fp = int(input("Por favor, ingrese un valor entre 1 y 2: "))
    envio = Envio(cp, df, tp, fp)
    return envio


def add_final_bin(envio, file_name):
    arch = open(file_name, "ab")
    data = envio.codigo_postal + "," + envio.direccion_fisica + "," + str(envio.tipo_envio) + "," + str(envio.forma_pago)
    pickle.dump(data, arch)
    arch.close()


# Punto 3
def read_bin(name_arch):
    arch = open(name_arch, "rb")
    tam = os.path.getsize(name_arch)
    while arch.tell() < tam:
        data = pickle.load(arch)
        cod_postal, dir_fisica, tipo_envio, forma_pago = get_data_bin(data)
        print(f"{cod_postal} {dir_fisica} {tipo_envio} {forma_pago} {determinar_pais(cod_postal)}")
    arch.close()


def get_data_bin(cadena):
    data = ["", "", "", ""]
    concatenacion_letras = ""
    i = 0
    for letra in cadena:
        if letra == "," or letra == '\n':
            data[i] = concatenacion_letras
            concatenacion_letras = ""
            i += 1
        else:
            concatenacion_letras += letra
    return data[0], data[1], data[2], data[3]


def determinar_pais(cod_postal):
    cp = cod_postal
    destino = "Otro"
    letrasCP_AR = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # letras segun ISO 3166
    if len(cp) == 8 and cp[0].isalpha() and cp[1:5].isdigit() and cp[5:].isalpha():
        if cp[0].upper() in letrasCP_AR:
            destino = "Argentina"
    elif len(cp) == 4 and cp.isdigit():
        destino = "Bolivia"
    elif len(cp) == 9 and cp[:5].isdigit() and cp[5] == '-' and cp[6:].isdigit():
        destino = "Brasil"
    elif len(cp) == 7 and cp.isdigit():
        destino = "Chile"
    elif len(cp) == 6 and cp.isdigit():
        destino = "Paraguay"
    elif len(cp) == 5 and cp.isdigit():
        destino = "Uruguay"
    return destino


# Punto 4
def buscar_por_cod_postal(cp, file_name):
    arch = open(file_name, "rb")
    tam = os.path.getsize(file_name)
    cp_encontrados = 0
    while arch.tell() < tam:
        data = pickle.load(arch)
        cod_postal, dir_fisica, tipo_envio, forma_pago = get_data_bin(data)
        if cp == cod_postal:
            print(f"{cod_postal} {dir_fisica} {tipo_envio} {forma_pago} {determinar_pais(cod_postal)}")
            cp_encontrados += 1
    print(f"La cantidad de registros con codigo postal {cp} encontados fue de: {cp_encontrados}")
    arch.close()


# Punto 5
def buscar_por_direccion(direccion, file_name):
    arch = open(file_name, "rb")
    tam = os.path.getsize(file_name)
    cp_encontrados = 0
    while arch.tell() < tam:
        data = pickle.load(arch)
        cod_postal, dir_fisica, tipo_envio, forma_pago = get_data_bin(data)
        if direccion == dir_fisica:
            print(f"{cod_postal} {dir_fisica} {tipo_envio} {forma_pago} {determinar_pais(cod_postal)}")
            return
    print(f"No se ha encontrado registro con la direccion {direccion}")
    arch.close()


# Punto 8
def calc_promedio(file_name):
    arch = open(file_name, "rb")
    tam = os.path.getsize(file_name)
    sum_importe = 0
    c_envios = 0
    contador = 0
    promedio = 0
    while arch.tell() < tam:
        data = pickle.load(arch)
        if contador == 0 or contador == 1:
            pass
        else:
            cod_postal, dir_fisica, tipo_envio, forma_pago = get_data_bin(data)
            sum_importe += obtener_importe(cod_postal, tipo_envio, forma_pago)
            c_envios += 1
        contador += 1
    if c_envios != 0:
        promedio = "{:.2f}".format(sum_importe / c_envios)
        promedio = float(promedio)
    arch.close()
    return promedio


def obtener_importe(cod_postal, tipo_carta, forma_pago):
    cp = cod_postal
    tipo = int(tipo_carta)
    pago = int(forma_pago)
    precios_nacionales = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    ajuste = 1.5  # Ajuste por defecto para "Otros" países
    letrasCP_AR = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # letras segun ISO 3166
    # condiciones para Argentina
    if len(cp) == 8 and cp[0].isalpha() and cp[1:5].isdigit() and cp[5:].isalpha():
        if cp[0].upper() in letrasCP_AR:
            ajuste = 1.0
    # condiciones para Bolivia
    elif len(cp) == 4 and cp.isdigit():
        ajuste = 1.2
    # condiciones para Brasil
    elif len(cp) == 9 and cp[:5].isdigit() and cp[5] == '-' and cp[6:].isdigit():
        if cp[0] == '8' or cp[0] == '9':
            ajuste = 1.2
        elif cp[0] in '0123':
            ajuste = 1.25
        else:
            ajuste = 1.3
    # condiciones para Chile
    elif len(cp) == 7 and cp.isdigit():
        ajuste = 1.25
    # condiciones para Paraguay
    elif len(cp) == 6 and cp.isdigit():
        ajuste = 1.2
    # condiciones para Uruguay
    elif len(cp) == 5 and cp.isdigit():
        if cp[0] == '1':
            ajuste = 1.2
        else:
            ajuste = 1.25
    # Calculamos el importe inicial
    inicial = int(precios_nacionales[tipo] * ajuste)
    # Calculamos el importe final
    final = inicial
    if pago == 1:
        final = int(inicial * 0.9)
    return final


def main():
    file_name = "datos.dat"
    envios = []
    arrSuma_Envios = []
    f_run_program = True
    control = None
    while f_run_program:
        op = menu()
        if op == 1:
            ##cop_csv_to_bin("")
            punto1()
        elif op == 2:
            nuevo_envio = crear_envio()
            add_final_bin(nuevo_envio, file_name)
        elif op == 3:
            read_bin("datos.dat")
        elif op == 4:
            cp = input("Ingrese el codigo postal a buscar: ")
            buscar_por_cod_postal(cp, file_name)
        elif op == 5:
            direccion = input("Ingrese la direccion a buscar: ")
            buscar_por_direccion(direccion, file_name)
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            prom = calc_promedio(file_name)
            print(f"Promedio es: {prom}")
        else:
            f_run_program = False


if __name__ == '__main__':
    main()

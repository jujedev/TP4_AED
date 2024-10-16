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
    data = envio.codigo_postal + "," + envio.direccion_fisica + "," + str(envio.tipo_envio) + "," + str(
        envio.forma_pago)
    pickle.dump(data, arch)
    arch.close()


# Punto 3
def read_bin(name_arch):
    if not os.path.exists(name_arch):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("No existe el archivo binario, por favor cargue uno")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return
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
    while arch.tell() < tam:
        data = pickle.load(arch)
        cod_postal, dir_fisica, tipo_envio, forma_pago = get_data_bin(data)
        if direccion == dir_fisica:
            print(f"{cod_postal} {dir_fisica} {tipo_envio} {forma_pago} {determinar_pais(cod_postal)}")
            return
    print(f"No se ha encontrado registro con la direccion {direccion}")
    arch.close()


# Punto 6

def punto6(file_name):
    if not os.path.exists(file_name):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("No existe el archivo binario, por favor cargue uno")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return

    n = 7
    m = 2
    vec2d = [0] * n
    for f in range(n):
        vec2d[f] = [0] * m

    txt_tipo_envio = 7 * [0]
    txt_tipo_envio[0] = "Simple - Peso menor a 20g"
    txt_tipo_envio[1] = "Simple - Peso entre 20g y 150g"
    txt_tipo_envio[2] = "Simple - Peso entre a 150g y 500g"
    txt_tipo_envio[3] = "Certificada - Peso menor a 150g"
    txt_tipo_envio[4] = "Certificada - Peso entre a 150g y 500g"
    txt_tipo_envio[5] = "Expresa - Peso menor a 150g"
    txt_tipo_envio[6] = "Expresa - Peso entre a 150g y 500g"

    txt_forma_pago = 2 * [0]
    txt_forma_pago[0] = "Efectivo"
    txt_forma_pago[1] = "Tarjeta de Credito"

    arch = open(file_name, "rb")
    tam = os.path.getsize(file_name)
    contador = 0
    while arch.tell() < tam:
        data = pickle.load(arch)
        if contador == 0 or contador == 1:
            pass
        else:
            cod_postal, dir_fisica, tipo_envio, forma_pago = get_data_bin(data)

            vec2d[int(tipo_envio)][(int(forma_pago)) - 1] += 1

        contador += 1

    filas = len(txt_tipo_envio)
    columnas = len(txt_forma_pago)
    for i in range(filas):
        for j in range(columnas):
            cant = vec2d[i][j]
            if cant > 0:
                print(f"Tipo envio: {txt_tipo_envio[i]} X Forma Pago: {txt_forma_pago[j]} Contiene: {cant}")

    return vec2d


# Punto 7

def punto7(vector):
    filas = len(vector)
    columnas = len(vector[0])

    for f in range(filas):
        sum_filas = 0
        for c in range(columnas):
            sum_filas += vector[f][c]

    for c in range(columnas):
        sum_col = 0
        for f in range(filas):
            sum_col += vector[f][c]

    print(f"Total Filas: {sum_filas}")
    print(f"Total Columnas: {sum_col}")


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


def generar_array_envios(envios, file_name, promedio):
    arch = open(file_name, "rb")
    tam = os.path.getsize(file_name)
    contador = 0
    while arch.tell() < tam:
        data = pickle.load(arch)
        if contador == 0 or contador == 1:
            pass
        else:
            cod_postal, dir_fisica, tipo_envio, forma_pago = get_data_bin(data)
            if obtener_importe(cod_postal, tipo_envio, forma_pago) > promedio:
                envios.append(Envio(cod_postal, dir_fisica, tipo_envio, forma_pago))
        contador += 1
    arch.close()


def mostrar_array(envios):
    for envio in envios:
        print(envio)


def ordenar_shellshort(envios):
    n = len(envios)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = envios[i]
            j = i
            while j >= gap and envios[j - gap].codigo_postal > temp.codigo_postal:
                envios[j] = envios[j - gap]
                j -= gap
            envios[j] = temp
        gap //= 2


def main():
    file_name = "datos.dat"
    envios = []
    vector = None
    f_run_program = True

    while f_run_program:
        op = menu()
        if op == 1:
            punto1()
        elif op == 2:
            nuevo_envio = crear_envio()
            add_final_bin(nuevo_envio, file_name)
        elif op == 3:
            read_bin("datos.dat")
        elif op == 4:

            if not os.path.exists(file_name):
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("No existe el archivo binario, por favor cargue uno")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                cp = input("Ingrese el codigo postal a buscar: ")
                buscar_por_cod_postal(cp, file_name)
        elif op == 5:
            if not os.path.exists(file_name):
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("No existe el archivo binario, por favor cargue uno")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                direccion = input("Ingrese la direccion a buscar: ")
                buscar_por_direccion(direccion, file_name)
        elif op == 6:
            vector = punto6(file_name)
        elif op == 7:
            if vector is None:
                print("Seleccione antes la opcion 6")
            else:
                punto7(vector)
        elif op == 8:
            if not os.path.exists(file_name):
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("No existe el archivo binario, por favor cargue uno")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                prom = calc_promedio(file_name)
                print(f"Promedio es: {prom}")
                generar_array_envios(envios, file_name, prom)
                ordenar_shellshort(envios)
                mostrar_array(envios)
        else:
            f_run_program = False


if __name__ == '__main__':
    main()

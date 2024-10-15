import pickle

class Envio:
    def __init__(self, codigo_postal, direccion, tipo_envio, forma_pago):
        self.codigo_postal = codigo_postal
        self.direccion = direccion
        self.tipo_envio = tipo_envio
        self.forma_pago = forma_pago

def check_dir(direccion):
    cl = cd = 0
    td = False
    ant = " "

    for car in direccion:
        if car in " .":
            if cd > 0 and cl == 0:
                td = True
            cl = cd = 0
            ant = " "
        else:
            if car.isdigit():
                cd += 1
            elif car.isalpha():
                cl += 1
            else:
                return False

            if ant.isupper() and car.isupper():
                return False

            ant = car
    if cd > 0 and cl == 0:
        td = True

    return td

def mostrar_registros(bin_file):
    envios = []
    f = open(bin_file, 'rb')
    while True:
        registro = f.read()
        if not registro:
            break
        envios.append(pickle.loads(registro))
    f.close()

    confirmacion = input("¿Desea ver todos los registros? (s/n): ")
    if confirmacion != "s":
        m = int(input("Indique la cantidad de registros a mostrar: "))
        for envio in envios[:m]:
            pais = indicar_paises(envio.codigo_postal)
            print(f"{envio.codigo_postal} - {envio.direccion} - {envio.tipo_envio} - {envio.forma_pago} - {pais}")
    else:
        for envio in envios:
            pais = indicar_paises(envio.codigo_postal)
            print(f"{envio.codigo_postal} - {envio.direccion} - {envio.tipo_envio} - {envio.forma_pago} - {pais}")

def leer_archivo(csv_file):
    envios = []
    f = open(csv_file, 'r', encoding="utf-8")
    lines = f.readlines()[2:]
    f.close()
    for line in lines:
        datos = line.strip().split(',')
        envio = Envio(datos[0], datos[1], int(datos[2]), int(datos[3]))
        envios.append(envio)
    return envios

def crear_arreglo_desde_archivo(csv_file, bin_file):
    envios = leer_archivo(csv_file)
    f = open(bin_file, 'wb')
    pickle.dump(envios, f)
    f.close()
    print("Arreglo Creado Exitosamente")
    return envios

def contar_envios_por_tipo(bin_file):
    contadores = [0] * 7
    f = open(bin_file, 'rb')
    while True:
        registro = f.read()
        if not registro:
            break
        envio = pickle.loads(registro)
        contadores[envio.tipo_envio] += 1
    f.close()

    for i in range(7):
        print(f"Cantidad de envíos del tipo {i}: {contadores[i]}")

def importe_final_acumulado(bin_file):
    acumulador = [0] * 7
    f = open(bin_file, 'rb')
    while True:
        registro = f.read()
        if not registro:
            break
        envio = pickle.loads(registro)
        importe = final_amount(envio)
        acumulador[envio.tipo_envio] += importe
    f.close()
    return acumulador

def cargar_envio_por_teclado(bin_file):
    codigo_postal = input("Ingrese el código postal: ").strip()
    direccion = input("Ingrese la dirección: ").strip()

    while True: 
        tipo_envio_input = input("Ingrese el tipo de envío (0-6): ")
        if tipo_envio_input.isdigit():
            tipo_envio = int(tipo_envio_input)
            if 0 <= tipo_envio <= 6:
                break
            else:
                print("Tipo de envío inválido. Debe estar entre 0 y 6.")
        else:
            print("Entrada inválida. Debe ser un número entre 0 y 6.")

    while True:
        forma_pago_input = input("Ingrese la forma de pago (1: efectivo, 2: tarjeta de crédito): ")
        if forma_pago_input.isdigit():
            forma_pago = int(forma_pago_input)
            if forma_pago == 1 or forma_pago == 2:
                break
            else:
                print("Forma de pago inválida. Debe ser 1 o 2.")
        else:
            print("Entrada inválida. Debe ser un número 1 o 2.")

    envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago)
    f = open(bin_file, 'ab')
    pickle.dump(envio, f)
    f.close()

def buscar_por_direccion_y_tipo(bin_file, direccion, tipo_envio):
    f = open(bin_file, 'rb')
    while True:
        registro = f.read()
        if not registro:
            break
        envio = pickle.loads(registro)
        if envio.direccion == direccion and envio.tipo_envio == tipo_envio:
            print(f"Envio encontrado: {envio.codigo_postal}, {envio.direccion}, {envio.tipo_envio}, {envio.forma_pago}")
    f.close()

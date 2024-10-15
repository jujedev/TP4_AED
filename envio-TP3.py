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

# TODO-CONTROLAR QUE FUNCIONE------------------------------------------------------------------ #

def mostrar_registros(envios):
    # Ordenar manualmente utilizando el algoritmo de selección
    n = len(envios)
    for i in range(n-1):
        for j in range(i+1, n):
            if clave_orden(envios[i]) > clave_orden(envios[j]):
                envios[i], envios[j] = envios[j], envios[i]

    # Mostrar los registros
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

# -------------------------------------------------------------------- #

def leer_archivo():
    envios = []
    

    fd = "envios-tp3.txt"
    m = open(fd, "rt", encoding="utf-8")  # Abrir el archivo manualmente
    lines = m.readlines()
    m.close()  # Cerrar el archivo manualmente

    for line in lines[1:]:  # Saltar la línea de timestamp
        codigo_postal = line[:9].strip()
        direccion = line[9:29].strip()
        tipo_envio = int(line[29])
        forma_pago = int(line[30])
        envios.append(Envio(codigo_postal, direccion, tipo_envio, forma_pago))

    return envios  # Aquí el return está dentro de la función

# -------------------------------------------------------------------- #

def crear_arreglo_desde_archivo(envios):
    if envios:
        confirmacion = input("El arreglo ya contiene datos. ¿Desea eliminarlo y crear uno nuevo desde el archivo? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("Operación cancelada.")
            return envios  # No hacer nada y retornar el arreglo existente
    # Si el arreglo está vacío o el usuario confirma la eliminación
    print("Arreglo Creado Exitosamente")
    return leer_archivo()

# -------------------------------------------------------------------- #

def contar_envios_por_tipo(envios, tipo_control):
    contadores = [0] * 7
    for envio in envios:
        if tipo_control == "HC":  # Hard Control
            if check_dir(envio.direccion):  # Solo contar si la dirección es válida
                contadores[envio.tipo_envio] += 1
        elif tipo_control == "SC":  # Soft Control
            contadores[envio.tipo_envio] += 1  # Cuenta todos los envíos sin validar dirección

    for i in range(7):
        print(f"Cantidad de envíos del tipo {i}: {contadores[i]}")

# -------------------------------------------------------------------- #

def importe_final_acumulado(envios, tipo_control):
    acumulador = [0] * 7
    for envio in envios:
        if tipo_control == "HC":
            if check_dir(envio.direccion):
                importe = final_amount(envio)
                acumulador[envio.tipo_envio] += importe
        elif tipo_control == "SC":
            importe = final_amount(envio)
            acumulador[envio.tipo_envio] += importe
    return acumulador

# -------------------------------------------------------------------- #

def cargar_envio_por_teclado(envios):
    codigo_postal = input("Ingrese el código postal: ").strip()
    direccion = input("Ingrese la dirección: ").strip()

    while True:
        tipo_envio_input = input("Ingrese el tipo de envío (0-6): ")
        if tipo_envio_input.isdigit():  # Verifica si la entrada es numérica
            tipo_envio = int(tipo_envio_input)  # Convierte a entero después de verificar
            if 0 <= tipo_envio <= 6:
                break  # Sal del bucle si la entrada es válida
            else:
                print("Tipo de envío inválido. Debe estar entre 0 y 6.")
        else:
            print("Entrada inválida. Debe ser un número entre 0 y 6.")

    while True:
        forma_pago_input = input("Ingrese la forma de pago (1: efectivo, 2: tarjeta de crédito): ")
        if forma_pago_input.isdigit():  # Verifica si la entrada es numérica
            forma_pago = int(forma_pago_input)  # Convierte a entero después de verificar
            if forma_pago == 1 or forma_pago == 2:
                break  # Sal del bucle si la entrada es válida
            else:
                print("Forma de pago inválida. Debe ser 1 o 2.")
        else:
            print("Entrada inválida. Debe ser un número 1 o 2.")

    envios.append(Envio(codigo_postal, direccion, tipo_envio, forma_pago))

# -------------------------------------------------------------------- #

def clave_orden(envio):
    # Esta función define la clave de ordenamiento
    codigo_postal = envio.codigo_postal
    if codigo_postal.isdigit():
        return (len(codigo_postal), False, int(codigo_postal))  # Prioridad a código postal numérico
    else:
        return (len(codigo_postal), True, float('inf'))  # Prioridad baja para no numéricos

# -------------------------------------------------------------------- #

# -------------------------------------------------------------------- #

def buscar_por_direccion_y_tipo(envios, direccion, tipo_envio):
    for envio in envios:
        if envio.direccion == direccion and envio.tipo_envio == tipo_envio:
            print(f"Encontrado: {envio.codigo_postal} - {envio.direccion} - {envio.tipo_envio} - {envio.forma_pago}")
            return
    print("No se encontró ningún envío con esa dirección y tipo.")

# -------------------------------------------------------------------- #
# TODO ver if envio.forma_pago == 1 else 1
def buscar_por_codigo_postal(envios, codigo_postal):
    for envio in envios:
        if envio.codigo_postal == codigo_postal:
            envio.forma_pago = 2 if envio.forma_pago == 1 else 1
            print(f"Modificado: {envio.codigo_postal} - {envio.direccion} - {envio.tipo_envio} - {envio.forma_pago}")
            return
    print("No se encontró ningún envío con ese código postal.")

# -------------------------------------------------------------------- #

def final_amount(envio):
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[envio.tipo_envio]
    destino = indicar_paises(envio.codigo_postal)
    if destino == 'Argentina':
        inicial = monto
    else:
        if destino in ['Bolivia', 'Paraguay'] or (destino == 'Uruguay' and envio.codigo_postal[0] == '1'):
            inicial = int(monto * 1.20)
        elif destino == 'Chile' or (destino == 'Uruguay' and envio.codigo_postal[0] != '1'):
            inicial = int(monto * 1.25)
        elif destino == 'Brasil':
            if envio.codigo_postal[0] in ['8', '9']:
                inicial = int(monto * 1.20)
            else:
                if envio.codigo_postal[0] in ['0', '1', '2', '3']:
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    final = inicial
    if envio.forma_pago == 1:
        final = int(0.9 * inicial)

    return final

# -------------------------------------------------------------------- #

def indicar_paises(codigo_postal):
    n = len(codigo_postal)
    if n < 4 or n > 9:
        return 'Otro'

    if n == 8:
        if codigo_postal[0].isalpha() and codigo_postal[0] not in 'IO' and codigo_postal[1:5].isdigit() and codigo_postal[5:8].isalpha():
            return 'Argentina'
        else:
            return 'Otro'

    if n == 9:
        if codigo_postal[0:5].isdigit() and codigo_postal[5] == '-' and codigo_postal[6:9].isdigit():
            return 'Brasil'
        else:
            return 'Otro'

    if codigo_postal.isdigit():
        if n == 4:
            return 'Bolivia'
        if n == 7:
            return 'Chile'
        if n == 6:
            return 'Paraguay'
        if n == 5:
            return 'Uruguay'
    return 'Otro'

# -------------------------------------------------------------------- #

def tipo_envio_mayor_importe(acumulado):
    if not acumulado:  # Si el vector de acumulación no existe o está vacío
        return None, None, None

    # Calcular el importe total manualmente
    total_importe = 0
    for monto in acumulado:
        total_importe += monto

    if total_importe == 0:
        return None, None, None

    # Encontrar el tipo de envío con mayor importe acumulado
    tipo_mayor = 0
    monto_mayor = acumulado[0]
    for i in range(1, len(acumulado)):
        if acumulado[i] > monto_mayor:
            monto_mayor = acumulado[i]
            tipo_mayor = i

    # Calcular el porcentaje que representa el mayor importe sobre el total
    porcentaje_mayor = (monto_mayor / total_importe) * 100

    return tipo_mayor, monto_mayor, porcentaje_mayor

def calcular_importe_promedio(envios, tipo_control):
    if not envios:
        return None, None

    # Calcular el importe total de todos los envíos y el número de envíos
    total_importe = 0
    total_envios = 0
    for envio in envios:
        if tipo_control == "HC" and not check_dir(envio.direccion):
            continue
        total_importe += final_amount(envio)
        total_envios += 1

    if total_envios == 0:
        return None, None

    # Calcular el importe promedio
    promedio_importe = total_importe / total_envios

    # Contar cuántos envíos tienen un importe menor al promedio
    menores_que_promedio = 0
    for envio in envios:
        if final_amount(envio) < promedio_importe:
            menores_que_promedio += 1

    return promedio_importe, menores_que_promedio

def control(arch):
    archivo = open(arch, "rt", encoding="utf-8")
    primera_linea = archivo.readline()
    
    if "HC" in primera_linea:
        archivo.close()
        return "HC"
    elif "SC" in primera_linea:
        archivo.close()
        return "SC"
    
    archivo.close()
    return None




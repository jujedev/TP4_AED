texto = open('envios-tp3.txt', 'rt')

def hc_o_sc(direccion):
    f_h = False
    f_hc = False
    ctrl = None
    for letra in direccion:
        if letra == "H":
            f_h = True
        if letra == "C" and f_h:
            f_hc = True
            f_h = False
    if f_hc == True:
        ctrl = "Hard Control"
    else:
        ctrl = "Soft Control"
    return ctrl


def cantidad_primer_cp(primer_cod_postal, cod_postal):
    valor = 0
    if primer_cod_postal == cod_postal:
        valor = 1
    return valor


def is_mayus(car):
    return 'A' <= car <= 'Z'


def is_digit(car):
    return '0' <= car <= '9'


def is_letra(car):
    abc = 'abcdefghijklmnñopqrstuvwxyz'
    return car.lower() in abc


def dir_val_no_val(direccion):
    """
    Hard  Control  (HC):  en  cada  envío  del  archivo  de  entrada,  se  debe  controlar  que  la  dirección  de
    destino tenga solo letras y dígitos, y que no haya dos mayúsculas seguidas, y que haya al menos una
    palabra  compuesta  sólo  por  dígitos.  Será  considerado  válido  el  envío  solo  si  pasa  la  verificación
    indicada aquí.
    """
    f_valid = f_pm = f_sm = f_nidl = False
    sm = nidl = False
    tiene_dos_mayus = palabra_solo_digito = no_letra_ni_num = False
    f_id = True
    for letra in direccion:
        if letra == " " or letra == ".":
            if f_id == True:
                palabra_solo_digito = True
            f_id = True

            if f_sm == True:
                tiene_dos_mayus = True
            f_pm = False
            f_sm = False
        else:
            # Verificamos que la direccion no tenga 2 mayusculas seguidas
            if is_mayus(letra) == True and f_pm == True:
                f_sm = True
                f_pm = False
            if is_mayus(letra) == True:
                f_pm = True
            # Verificamos que la palabra este compuesta unicamente por digitos
            if is_digit(letra) != True:
                f_id = False
            # Verficamos que la direccion este compuesta unicamente por letra y/o digitos (no caracteres especiales)
            if not(is_letra(letra) == True or is_digit(letra) == True):
                no_letra_ni_num = True

    if not(tiene_dos_mayus) and palabra_solo_digito and not(no_letra_ni_num):
        f_valid = True
    else:
        f_valid = False
    return f_valid


def tipo_de_carta(tipo_envio):
    tipo_envio = int(tipo_envio)
    if 0 <= tipo_envio <= 2:
        val = '1'
    elif 3 <= tipo_envio <= 4:
        val = '2'
    else:
        val = '3'
    return val


def may(num_1, num_2, num_3):
    may = None
    if num_1 > num_2 and num_1 > num_3:
        may = 'Carta Simple'
    elif num_2 > num_3:
        may = 'Carta Certificada'
    else:
        may = 'Carta Expresa'
    return may


def suma_acumulado(cod_postal, tipo_carta, forma_pago):
    # ENTRADAS
    cp = cod_postal
    #direccion = input("Dirección del lugar de destino: ")
    tipo = int(tipo_carta)
    pago = int(forma_pago)

    # PROCESO
    # se define la tabla de precios y descuentos en una Tupla
    precios_nacionales = (1100, 1800, 2450, 8300, 10900, 14300, 17900)

    # definicion de variables
    destino = "Otro"
    provincia = "No aplica"
    ajuste = 1.5  # Ajuste por defecto para "Otros" países
    letrasCP_AR = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # letras segun ISO 3166

    # Verificamos el país y la provincia de destino

    # condiciones para Argentina
    if len(cp) == 8 and cp[0].isalpha() and cp[1:5].isdigit() and cp[5:].isalpha():
        if cp[0].upper() in letrasCP_AR:
            destino = "Argentina"
            ajuste = 1.0  # No hay ajuste para Argentina
            if cp[0].upper() == "A":
                provincia = "Salta"
            elif cp[0].upper() == "B":
                provincia = "Provincia de Buenos Aires"
            elif cp[0].upper() == "C":
                provincia = "Ciudad Autónoma de Buenos Aires"
            elif cp[0].upper() == "D":
                provincia = "San Luis"
            elif cp[0].upper() == "E":
                provincia = "Entre Ríos"
            elif cp[0].upper() == "F":
                provincia = "La Rioja"
            elif cp[0].upper() == "G":
                provincia = "Santiago del Estero"
            elif cp[0].upper() == "H":
                provincia = "Chaco"
            elif cp[0].upper() == "J":
                provincia = "San Juan"
            elif cp[0].upper() == "K":
                provincia = "Catamarca"
            elif cp[0].upper() == "L":
                provincia = "La Pampa"
            elif cp[0].upper() == "M":
                provincia = "Mendoza"
            elif cp[0].upper() == "N":
                provincia = "Misiones"
            elif cp[0].upper() == "P":
                provincia = "Formosa"
            elif cp[0].upper() == "Q":
                provincia = "Neuquén"
            elif cp[0].upper() == "R":
                provincia = "Río Negro"
            elif cp[0].upper() == "S":
                provincia = "Santa Fe"
            elif cp[0].upper() == "T":
                provincia = "Tucumán"
            elif cp[0].upper() == "U":
                provincia = "Chubut"
            elif cp[0].upper() == "V":
                provincia = "Tierra del Fuego"
            elif cp[0].upper() == "W":
                provincia = "Corrientes"
            elif cp[0].upper() == "X":
                provincia = "Córdoba"
            elif cp[0].upper() == "Y":
                provincia = "Jujuy"
            elif cp[0].upper() == "Z":
                provincia = "Santa Cruz"
    # condiciones para Bolivia
    elif len(cp) == 4 and cp.isdigit():
        destino = "Bolivia"
        ajuste = 1.2
    # condiciones para Brasil
    elif len(cp) == 9 and cp[:5].isdigit() and cp[5] == '-' and cp[6:].isdigit():
        destino = "Brasil"
        if cp[0] == '8' or cp[0] == '9':
            ajuste = 1.2
        elif cp[0] in '0123':
            ajuste = 1.25
        else:
            ajuste = 1.3
    # condiciones para Chile
    elif len(cp) == 7 and cp.isdigit():
        destino = "Chile"
        ajuste = 1.25
    # condiciones para Paraguay
    elif len(cp) == 6 and cp.isdigit():
        destino = "Paraguay"
        ajuste = 1.2
    # condiciones para Uruguay
    elif len(cp) == 5 and cp.isdigit():
        destino = "Uruguay"
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


def menor_imp_br(cod_postal, tipo_envio, forma_pago, menimp, mencp):
    cp = cod_postal
    r_mencp = mencp
    tipo = int(tipo_envio)
    pago = int(forma_pago)
    precios_nacionales = (1100, 1800, 2450, 8300, 10900, 14300, 17900)

    destino = "Otro"
    ajuste = 1.5  # Ajuste por defecto para "Otros" países
    # condiciones para Brasil
    if len(cp) == 9 and cp[:5].isdigit() and cp[5] == '-' and cp[6:].isdigit():
        destino = "Brasil"
        if cp[0] == '8' or cp[0] == '9':
            ajuste = 1.2
        elif cp[0] in '0123':
            ajuste = 1.25
        else:
            ajuste = 1.3
        inicial = int(precios_nacionales[tipo] * ajuste)
        final = inicial
        if pago == 1:
            final = int(inicial * 0.9)
        if final < menimp:
            menimp = final
            r_mencp = cp
    else:
        final = 0
    return menimp, r_mencp


def  envio_exterior(cod_postal):
    letrasCP_AR = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # letras segun ISO 3166
    cp = cod_postal
    env_ext = 0
    if len(cp) == 8 and cp[0].isalpha() and cp[1:5].isdigit() and cp[5:].isalpha() and cp[0].upper() in letrasCP_AR:
        env_ext = 0
    else:
        env_ext = 1
    return env_ext


def porcentaje(n1, n2):
    if n2 != 0:
        pc = n1 * 100 / n2
    else:
        pc = 0
    return pc


def envios_bs_as(cod_postal):
    envio = 0
    cp = cod_postal
    letrasCP_AR = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # letras segun ISO 3166
    if len(cp) == 8 and cp[0].isalpha() and cp[1:5].isdigit() and cp[5:].isalpha():
        if cp[0].upper() in letrasCP_AR:
            if cp[0].upper() == "B": # or cp[0].upper() == "C":
                envio = 1
    return envio


def promedio(sum_env_bs_as, cant_env_bs_as):
    prom = 0
    if cant_env_bs_as != 0:
        prom = sum_env_bs_as / cant_env_bs_as
    return prom


def sum_envios_bs_as(cod_postal, tip_envio, fo_pago):
    cp = cod_postal
    tipo = int(tip_envio)
    pago = int(fo_pago)
    precios_nacionales = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    ajuste = 1.5
    letrasCP_AR = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    final = 0
    if len(cp) == 8 and cp[0].isalpha() and cp[1:5].isdigit() and cp[5:].isalpha():
        if cp[0].upper() in letrasCP_AR:
            ajuste = 1.0  # No hay ajuste para Argentina
            if cp[0].upper() == "B": # or cp[0].upper() == "C":
                inicial = int(precios_nacionales[tipo] * ajuste)
                final = inicial
                if pago == 1:
                    final = int(inicial * 0.9)
    return final


def main(texto):
    control = tipo_mayor = mencp = primer_cp = None
    cedvalid = cedinvalid = imp_acu_total = ccs = ccc = cce = ce_ext = c_env_bs = prom = cant_env_ext = sum_env_bs_as = 0
    f_cedvalid = False
    cant_primer_cp = tipo_envio = forma_pago = cantidad_envios = porc = suma_env_bs = cant_env = cant_env_bs_as = 0
    menimp = 10000000

    contador = 1
    for linea in texto:
        linea = linea.replace('\n','')
        if contador == 1:
            # RESPUESTA PUNTO 1
            control = hc_o_sc(linea)
        else:
            cp = linea[0:9].strip()
            direccion = linea[9:29].strip()
            tipo_envio = linea[29]
            forma_pago = linea[30]
            cant_env += 1
            if contador == 2:
            # RESPUESTA PUNTO 9
                primer_cp = cp
            # RESPUESTA PUNTO 10
            cant_primer_cp += cantidad_primer_cp(primer_cp, cp)
            # RESPUESTA PUNTO 2 y 3
            if control == "Hard Control":
                if dir_val_no_val(direccion) == True:
                    cedvalid += 1
                # RESPUESTA PUNTO 4
                    imp_acu_total += suma_acumulado(cp, tipo_envio, forma_pago)
                # RESPUESTA PUNTO 5, 6 Y 7
                    tipo_carta = tipo_de_carta(tipo_envio)
                    if tipo_carta == '1':
                        ccs += 1
                    elif tipo_carta == '2':
                        ccc += 1
                    else:
                        cce += 1
                    cant_env_ext += envio_exterior(cp)
                    cant_env_bs_as += envios_bs_as(cp)
                    sum_env_bs_as += sum_envios_bs_as(cp, tipo_envio, forma_pago)
                else:
                    cedinvalid += 1
            # RESPUESTA PUNTO 11 y 12
                menimp, mencp = menor_imp_br(cp, tipo_envio, forma_pago, menimp, mencp)
            else:
                # RESPUESTA PUNTO 2 y 3
                cedvalid += 1
                # RESPUESTA PUNTO 4
                imp_acu_total += suma_acumulado(cp, tipo_envio, forma_pago)
                # RESPUESTA PUNTO 5, 6 Y 7
                tipo_carta = tipo_de_carta(tipo_envio)
                if tipo_carta == '1':
                    ccs += 1
                elif tipo_carta == '2':
                    ccc += 1
                else:
                    cce += 1
                cant_env_ext += envio_exterior(cp)
                cant_env_bs_as += envios_bs_as(cp)
                sum_env_bs_as += sum_envios_bs_as(cp, tipo_envio, forma_pago)
                cedinvalid = 0
                # RESPUESTA PUNTO 11 y 12
                menimp, mencp = menor_imp_br(cp, tipo_envio, forma_pago, menimp, mencp)
        contador += 1
    # RESPUESTA PUNTO 8
    tipo_mayor = may(ccs, ccc, cce)
    # RESPUESTA PUNTO 13
    porc = int(porcentaje(cant_env_ext,cant_env))
    # RESPUESTA PUNTO 14
    prom = int(promedio(sum_env_bs_as, cant_env_bs_as))
    print(' (r1) - Tipo de control de direcciones:', control) # Listo
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid) # Listo
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid) # Listo
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total) # Listo
    print(' (r5) - Cantidad de cartas simples:', ccs) # Listo
    print(' (r6) - Cantidad de cartas certificadas:', ccc) # Listo
    print(' (r7) - Cantidad de cartas expresas:', cce) # Listo
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor) # Listo
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp) # Listo
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp) # Listo
    print('(r11) - Importe menor pagado por envios a Brasil:', menimp) # Listo
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp) # Listo
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc) # Listo
    print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom) # Listo


main(texto)
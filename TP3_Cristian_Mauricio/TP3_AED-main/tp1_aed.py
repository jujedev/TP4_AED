# ENTRADAS
cp = input("Ingrese el código postal del lugar de destino: ")
#direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

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

# SALIDAS
print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)

import pickle

class Envio:
    def __init__(self, codigo_postal, direccion_fisica, tipo_envio, forma_pago):
        self.codigo_postal = codigo_postal
        self.direccion_fisica = direccion_fisica
        self.tipo_envio = tipo_envio
        self.forma_pago = forma_pago

def crear_archivo_binario(csv_file, bin_file):
    with open(csv_file, 'r') as f:
        lines = f.readlines()[2:]  # Ignorar las dos primeras líneas
    envios = []
    for line in lines:
        datos = line.strip().split(',')
        envio = Envio(datos[0], datos[1], int(datos[2]), int(datos[3]))
        envios.append(envio)
    with open(bin_file, 'wb') as f:
        pickle.dump(envios, f)

def cargar_envio(bin_file):
    codigo_postal = input("Ingrese el código postal: ")
    direccion_fisica = input("Ingrese la dirección física: ")
    tipo_envio = int(input("Ingrese el tipo de envío (0-6): "))
    forma_pago = int(input("Ingrese la forma de pago (1: efectivo, 2: tarjeta de crédito): "))
    envio = Envio(codigo_postal, direccion_fisica, tipo_envio, forma_pago)
    with open(bin_file, 'ab') as f:
        pickle.dump(envio, f)

def mostrar_envios(bin_file):
    with open(bin_file, 'rb') as f:
        try:
            while True:
                envio = pickle.load(f)
                print(f"CP: {envio.codigo_postal}, Dirección: {envio.direccion_fisica}, Tipo: {envio.tipo_envio}, Pago: {envio.forma_pago}")
        except EOFError:
            pass

# Ejemplo de uso
csv_file = 'envios.csv'
bin_file = 'envios.bin'

# Crear archivo binario desde CSV
crear_archivo_binario(csv_file, bin_file)

# Cargar un nuevo envío
cargar_envio(bin_file)

# Mostrar todos los envíos
mostrar_envios(bin_file)





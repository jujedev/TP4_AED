"""
1. Crear el archivo binario de registros de forma que contenga todos los datos de todos los envios
guardados en el archivo de texto envios-tp4.csv que se provee junto con este enunciado. Cada vez
que se elija esta opción, el archivo binario debe ser creado de nuevo desde cero, perdiendo todos
los registros que ya hubiese contenido. Asegúrese de que antes de eliminar el viejo archivo, se
muestre en pantalla un mensaje de advertencia al usuario de forma que tenga la opción de cancelar
la operación. Repetimos: NO DEBE CREAR UN ARREGLO DE REGISTROS/OBJETOS, sino directamente
pasar del archivo de texto al archivo binario. Y salvo en el punto 7 de este listado de procesos, EN
NINGÚN OTRO PUNTO DEBE CREAR TAL ARREGLO, sino trabajar directamente con los datos
contenidos en el archivo binario.
2. Cargar por teclado los datos de un envio, aplicando procesos de validación para cada campo, y
agregar un registro con esos datos directamente al final del archivo binario. Cada vez que se elija
esta opción, el nuevo registro debe agregarse al final del archivo binario, sin perder ninguno de los
registros que el archivo ya contenía. Si el archivo no existiese, debe ser creado y luego agregar el
registro cargado.
3. Mostrar todos los datos de todos los registros del archivo binario, tal como están grabados (sin
ningún proceso de ordenamiento previo). Cada registro debe ocupar una sola línea en pantalla, y
debe mostrarse también el nombre del país al que corresponde el código postal.
4. Mostrar todos los registros del archivo binario cuyo código postal sea igual a cp, siendo cp un valor
que se carga por teclado. Al final del listado mostrar una línea adicional indicando cuántos registros
se mostraron.
3
5. Buscar si existe en el archivo binario un registro cuya dirección postal sea igual a d, siendo d un valor
que se carga por teclado. Si existe mostrar el registro completo. Si no existe indicar con un mensaje.
La búsqueda debe detenerse al encontrar el primer registro que coincida con el criterio pedido.
6. Determinar y mostrar la cantidad de envíos de cada combinación posible entre tipo de envío y forma
de pago en el archivo binario. Como son siete tipos de envíos posibles y son dos las formas de pago
posibles, entonces se trata de 7 * 2 = 14 contadores, que obviamente deben ser gestionados en una
matriz de conteo. Muestre solo los contadores cuyo valor final sea diferente de cero. Observación:
ni siquiera se les ocurra plantear un esquema de 15 condiciones y 15 contadores separados… Esto se
resuelve con una matriz de conteo o nada.
7. En base a la matriz que se pidió generar en el ítem anterior, muestre la cantidad total de envíios
contados por cada tipo de envío posible, y la cantidad total de envíos contados por cada forma de
pago posible. Es decir, se pide por un lado, totalizar las filas de esa matriz, y por otro, totalizar las
columnas.
8. Recorrer el archivo binario, y calcular el importe promedio pagado entre todos los envíos que figuran
en el archivo. Y ahora sí, generar en memoria un arreglo de registros/objetos con todos los envíos
del archivo binario cuyo importe sea mayor al promedio que acaba de calcular. Muestre el arreglo,
pero ordenado de menor a mayor de acuerdo al código postal. En este punto, los programadores
deben considerar que la cantidad de datos en el vector podría ser realmente un número grande o
muy grande, y por lo tanto, no deberían aplicar un método de ordenamiento simple. Tienen al menos
el Shellsort explicado en clases. El archivo de entrada en formato .csv tiene 100000 (cien mil) líneas
de datos, por lo que muy posiblemente el tamaño del "arreglito" que les tamos pidiendo ronde los
50000 (cincuenta mil) objetos... Deduzcan lo que deben hacer…
"""

def principal():
  print("Como estas")

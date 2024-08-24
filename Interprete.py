from funciones import Obtener_tipo_de_dato
from aux_funcion import limpiar_archivo

limpiar_archivo('output')
Flag = True
i= 0

with open('codigo.txt', 'r') as archivo:
    cadena = archivo.readline()
    while cadena:
        i += 1
        cadena = cadena.strip()  # Quitamos espacios en blanco y saltos de línea
        if cadena:  # Si la línea no está vacía
            Flag = Obtener_tipo_de_dato(cadena, Flag , i)  # Llama a tu función para procesar la línea
        cadena = archivo.readline()
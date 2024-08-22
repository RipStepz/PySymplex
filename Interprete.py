from funciones import Obtener_tipo_de_dato, prueba, MOSTRAR
from aux_funcion import limpiar_archivo

# Obtener_tipo_de_dato("DEFINE $_Largo")
# Obtener_tipo_de_dato("DEFINE $_Ancho")
# Obtener_tipo_de_dato("DEFINE $_Area")
# Obtener_tipo_de_dato("DEFINE $_Texto")
# Obtener_tipo_de_dato("DP $_Largo ASIG 6")
# Obtener_tipo_de_dato("DP $_Ancho ASIG 5")
# Obtener_tipo_de_dato("DP $_Area * $_Largo $_Ancho")
# Obtener_tipo_de_dato("DP $_Texto ASIG #La altura del rectangulo es #")
# Obtener_tipo_de_dato("DP $_Texto + $_Texto $_Area")
# Obtener_tipo_de_dato("DEFINE $_Var2")
# Obtener_tipo_de_dato("DP $_Var1 ASIG 6")
# Obtener_tipo_de_dato("DP $_Var2 ASIG 8")
# Obtener_tipo_de_dato("DP $_Var1 + $_Var2 $_Var1")
##prueba()
limpiar_archivo('archivo.txt')
Flag = True


with open('codigo.txt', 'r') as archivo:
    linea = archivo.readline()
    while linea:
        linea = linea.strip()  # Quitamos espacios en blanco y saltos de línea
        if linea:  # Si la línea no está vacía
            Obtener_tipo_de_dato(linea)  # Llama a tu función para procesar la línea
        linea = archivo.readline()

##prueba()
from RegEx import Int, Bool_RegEx
import re

def Boolenizar(cadena):
    '''
    ***
    cadena : String a pasar a booleano
    ...
    ***
    Retorna un booleano o None
    ***
    Compara el string con true, para que guarde true o false en una variable y lo retorna, caso contrario retorna None
    '''
    if re.match(Bool_RegEx, cadena):
        Valor_bool = (cadena == "True")
        return Valor_bool
    else:
        None

def Obtener_variable(cadena , n):
    '''
    ***
    cadena : string
    n : entero
    ...
    ***
    La variable que busco
    ***
    Encuentro el $ que significa que encontre la variable y despues el espacio con eso puedo obtener la variable del string general
    y retorno la variable, en caso de seleccionarese 1 como n no sera hasta el espacio sino que el final
    2 sera hasta un paretesis
    '''
    inicio = cadena.find('$')
    fin = cadena.find(' ', inicio)
    if n == 1:
        return cadena[inicio:].strip()
    if n==2:
        fin = cadena.find(')', inicio)
    variable = cadena[inicio:fin].strip()
    return variable

def Obtener_informacion_a_almacenar(cadena):
    '''
    ***
    cadena : string
    ...
    ***
    Retorna lo que quiero almacenar con el asig
    ***
    Encuentro el asig porque lo que necesito es lo que le sigue y retorno valor que es lo que le sigue a "ASIG"
    '''
    inicio_asig = cadena.find('ASIG')
    inicio_valor = inicio_asig + len('ASIG')
    valor = cadena[inicio_valor:].strip()
    return valor

def Control_tipo_dato(cadena):
    '''
    ***
    cadena : string
    ***
    Retorna, el string mismo, el string boolenizado o el string convertido a numero
    ***
    Para llegar al retorno esperado uso las RegEx para comprobar a que tipo de dato me estoy enfrentado
    '''
    cadena = cadena.strip()  

    if re.match(Int, cadena):
        return int(cadena)
    
    elif re.match(Bool_RegEx, cadena):
        return Boolenizar(cadena)
    
    else:
        return cadena

def Auxiliar_Suma_string_int(cadena, n):
    '''
    ***
    cadena : string
    n: entero
    ...
    ***
    El string es retornado sin uno de los #
    ***
    Esta funcion dependiendo del n que le entregen (entre 1 y 2) quita un # (si n = 1 se quita el primer
    n=2 el segundo) y se retorna ese string

    '''
    if n == 1:
        # Eliminar el primer #
        return cadena[1:] if cadena.startswith('#') else cadena
    elif n == 2:
        # Eliminar el último #
        return cadena[:-1] if cadena.endswith('#') else cadena

def limpiar_archivo(nombre_archivo):
    '''
    ***
    nombre_archivo : string
    ...
    ***
    None
    ***
    vacia el archivo y tiene una forma de evitar vaciar algo que no exista
    '''
    try:
        with open(nombre_archivo, 'w') as archivo:
            pass  # Abre el archivo en modo escritura, lo que vacía su contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
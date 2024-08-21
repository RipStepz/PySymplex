import re
from RegEx import Int, String, Bool_RegEx, Procesamiento_datos, ASIG, Suma, Multiplicacion, Mayor_que,  Igual_que, Variable

Almacen_Variables = {}

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

def Obtener_variable(cadena):
    '''
    ***
    cadena : string
    ...
    ***
    La variable que busco
    ***
    Encuentro el $ que significa que encontre la variable y despues el espacio con eso puedo obtener la variable del string general
    y retorno la variable
    '''
    inicio = cadena.find('$')
    fin = cadena.find(' ', inicio)
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
    
def Asignacion(cadena):
    '''
    ***
    cadena : string
    ...
    ***
    No retorna nada solo controla la logica de el almacenamiento de las variables
    ***
    En el primer if me aseguro que la informacion que quiero almacenar no es una variable porque hay que tratar ese caso distinto
    con eso guardo en un diccionario con llave del nombre de la variable la info, en el caso de que info se encuentre en el diccionario, saco su info y la agregro
    en el caso de que no este en el diccionario, estoy tratando de asignar una variable que no existe, lo que tiene que tirar error
    '''
    Var = Obtener_variable(cadena)
    Info = Obtener_informacion_a_almacenar(cadena)
    
    if (bool(re.match(Variable, Info))):
        if Info not in Almacen_Variables:
            print("No se puede asignar una variable no existente a otra")
        else:
            Auxiliar = Almacen_Variables[Info]
            Almacen_Variables[Var] = Control_tipo_dato(Auxiliar)

    elif (Info not in Almacen_Variables):
        Almacen_Variables[Var] = Control_tipo_dato(Info)

def obtener_cosas_a_sumar(cadena, n):
    '''
    ***
    cadena : string
    n : entero
    ...
    ***
    retorna el primer o segundo valor dependiendo de cual se le pida a la funcion
    ***
    Cree una nueva Regex con el objetivo de poder crear dos grupos y extrear los valores
    luego simplemente retorno uno o el otro dependiendo de cual pidan en la funcion
    '''
    regex = r'\+\s*(' + Variable + r'|' + Int + r')\s+(' + Variable + r'|' + Int + r')'
    
    match = re.search(regex, cadena)
    if match:
       
        valor1 = match.group(1)
        valor1.strip()
        valor2 = match.group(2)
        valor2.strip()
        
        if n == 1:
            return valor1
        elif n == 2:
            return valor2

def Realizar_suma(cadena):
    '''
    ***
    cadena: string 
    ...
    ***
    No retorna nada, solo hace la suma de los numeros y los guarda en en el diccionario
    ***
    Tomo en cuenta todas las posibilidades que puede pasar con la suma y las resuelvo, en caso de ser una suma
    imposible printeo por consola "No se realizo suma, ya que estas sumando una variable que no esta definida"
    '''
    Numero_1 = obtener_cosas_a_sumar(cadena, 1)
    Numero_2 = obtener_cosas_a_sumar(cadena, 2)
    Variable_a_asignar = Obtener_variable(cadena)

    if (bool(re.match(Int, Numero_1))) and (bool(re.match(Int, Numero_2))):
        Sumado = int(Numero_1) + int(Numero_2)
        Almacen_Variables[Variable_a_asignar] = Sumado
    
    elif (bool(re.match(Int, Numero_1))) and (bool(re.match(Variable, Numero_2))) and (Numero_2 in Almacen_Variables):
        Numero_2 = Almacen_Variables[Numero_2]
        Sumado = int(Numero_1) + int(Numero_2)
        Almacen_Variables[Variable_a_asignar] = Sumado
    
    elif (bool(re.match(Variable, Numero_1))) and (bool(re.match(Int, Numero_2))) and (Numero_1 in Almacen_Variables):
        Numero_1 = Almacen_Variables[Numero_1]
        Sumado = int(Numero_1) + int(Numero_2)
        Almacen_Variables[Variable_a_asignar] = Sumado
    
    elif (bool(re.match(Variable, Numero_1))) and (bool(re.match(Variable, Numero_2))) and (Numero_1 in Almacen_Variables) and (Numero_2 in Almacen_Variables):
        Numero_1 = Almacen_Variables[Numero_1]
        Numero_2 = Almacen_Variables[Numero_2]
        Sumado = int(Numero_1) + int(Numero_2)
        Almacen_Variables[Variable_a_asignar] = Sumado
    else:
        print("No se realizo suma, ya que estas sumando una variable que no esta definida")        

def Obtener_tipo_de_dato(cadena):
    '''
    ***
    cadena : Cadena que cumpla con la RegEx Procesamiento_datos 
    ...
    ***
    Retorna el valor del dato que contenga la cadena, dependiendo del tipo de operación
    ***
    '''
    if re.match(ASIG, cadena):
        Asignacion(cadena)
        print("Se pide un ASIG")

    elif re.match(Suma, cadena):
        Realizar_suma(cadena)
        print("Se pide una suma")

    elif re.match(Multiplicacion, cadena):
        print("Se pide una multiplicación")

    elif re.match(Mayor_que, cadena):
        print("Se pide una operación de mayor que")

    elif re.match(Igual_que, cadena):
        print("Se pide una comparación de igualdad")

    else:
        print("No se ha detectado una operación válida")

    return None

def prueba():
    for clave, valor in Almacen_Variables.items():
        print(f"{clave}: {valor}")
        print(type(Almacen_Variables[clave]))
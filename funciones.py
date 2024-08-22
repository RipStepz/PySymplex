import re
from RegEx import Int, String, MOSTRAR_RegEx, Procesamiento_datos, ASIG, Suma, Multiplicacion, Mayor_que,  Igual_que, Variable, DEFINE_PATTERN
from Repetitivo import *
from aux_funcion import *
Almacen_Variables = {}

def DEFINE(cadena):
    '''
    ***
    cadena : string
    ...
    ***
    No hay retorno
    ***
    La funcion recicla una funcion con la que obtengo la variable y luego simplemente compruebo
    si ya existe la variable, si no existe si crea
    '''
    Var_para_dic = Obtener_variable(cadena , 1)
    
    if Var_para_dic not in Almacen_Variables:
        Almacen_Variables[Var_para_dic] = None
    else:
        print(Var_para_dic)
        print("No se puede reedifinir una variable")

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
    Var = Obtener_variable(cadena , 0)
    Info = Obtener_informacion_a_almacenar(cadena)

    if Var not in Almacen_Variables:
        print("No puedes asignar algo a una variable que no existe")
        return None
    
    if (bool(re.match(Variable, Info))):
        if Info not in Almacen_Variables:
            print("No se puede asignar una variable no existente a otra")
        else:
            Auxiliar = Almacen_Variables[Info]
            Almacen_Variables[Var] = Control_tipo_dato(Auxiliar)

    elif (Info not in Almacen_Variables):
        Almacen_Variables[Var] = Control_tipo_dato(Info)

def Realizar_suma(cadena):
    '''
    ***
    cadena: string 
    ...
    ***
    No retorna nada, solo hace la suma de los numeros y los guarda en el diccionario
    ***
    Tomo en cuenta todas las posibilidades que puede pasar con la suma y las resuelvo, en caso de ser una suma
    imposible printeo por consola "No se realizo suma, ya que estas sumando una variable que no esta definida"
    '''
    if obtener_cosas_a_Sumar(cadena, 1):

        Numero_1 = obtener_cosas_a_Sumar(cadena, 1)
        Numero_2 = obtener_cosas_a_Sumar(cadena, 2)
        Variable_a_asignar = Obtener_variable(cadena , 0)

        if Variable_a_asignar not in Almacen_Variables:
            print("No puedes asignar algo a una variable que no existe")
            return None
        
        if Numero_1 in Almacen_Variables:
            Numero_1 = Almacen_Variables[Numero_1]
        
        if Numero_2 in Almacen_Variables:
            Numero_2 = Almacen_Variables[Numero_2]
        
        Numero_1 = str(Numero_1) if Numero_1 is not None else ""
        Numero_2 = str(Numero_2) if Numero_2 is not None else ""
     
        if (bool(re.match(Int, Numero_1))) and (bool(re.match(Int, Numero_2))):
            Sumado = int(Numero_1) + int(Numero_2)
            Almacen_Variables[Variable_a_asignar] = Sumado
        
        elif (bool(re.match(String, Numero_1))) and (bool(re.match(Int, Numero_2))):
            Sumado = Auxiliar_Suma_string_int(Numero_1, 2) + Numero_2 + "#"
            Almacen_Variables[Variable_a_asignar] = Sumado ##este caso funciona
        
        elif (bool(re.match(Int, Numero_1))) and (bool(re.match(String, Numero_2))):
            Sumado = "#" + Numero_1 + Auxiliar_Suma_string_int(Numero_2, 1)
            Almacen_Variables[Variable_a_asignar] = Sumado
        
        elif (bool(re.match(Int, Numero_1))) and (bool(re.match(String, Numero_2))):
            Sumado = "#" + Numero_1 + Auxiliar_Suma_string_int(Numero_2, 1)
            Almacen_Variables[Variable_a_asignar] = Sumado

        elif (bool(re.match(String, Numero_1))) and (bool(re.match(String, Numero_2))):
            Sumado = Auxiliar_Suma_string_int(Numero_1, 2) + Auxiliar_Suma_string_int(Numero_2, 1)
            Almacen_Variables[Variable_a_asignar] = Sumado

        else:
            print("No se realizo suma, ya que estas sumando una variable que no esta definida")        

    else:
        return print("Suma invalida")

def Realizar_multiplicacion(cadena):
    '''
    ***
    cadena: string 
    ...
    ***
    No retorna nada, solo hace la multiplicacion de los numeros y los guarda en el diccionario
    ***
    Tomo en cuenta todas las posibilidades que puede pasar con la multiplicacion y las resuelvo, en caso de ser una multiplicacion
    imposible printeo por consola "No se realizo la multiplicacion, ya que estas multiplicacndo una variable que no esta definida"
    '''
    if obtener_cosas_a_multiplicar(cadena, 1):
        
        Numero_1 = obtener_cosas_a_multiplicar(cadena, 1)
        Numero_2 = obtener_cosas_a_multiplicar(cadena, 2)
        Variable_a_asignar = Obtener_variable(cadena , 0)

        if Variable_a_asignar not in Almacen_Variables:
            print("No puedes asignar algo a una variable que no existe")
            return None
        
        if Numero_1 in Almacen_Variables:
            Numero_1 = Almacen_Variables[Numero_1]
        
        if Numero_2 in Almacen_Variables:
            Numero_2 = Almacen_Variables[Numero_2]
        
        Numero_1 = str(Numero_1) if Numero_1 is not None else ""
        Numero_2 = str(Numero_2) if Numero_2 is not None else ""
     
        if (bool(re.match(Int, Numero_1))) and (bool(re.match(Int, Numero_2))):
            Sumado = int(Numero_1) * int(Numero_2)
            Almacen_Variables[Variable_a_asignar] = Sumado

        else:
            print("No se realizo la Multiplicacion, ya que estas multiplicando una variable que no esta definida")        

    else:
        return print("Multiplicacion invalida")

def Realizar_Mayor_que(cadena):
    '''
    ***
    cadena: string 
    ...
    ***
    Retorna un booleano.
    ***
    Me aseguro de tener los valores como string luego simplemente compara y retorna un bool
    '''
    if obtener_cosas_Mayor_que(cadena, 1):

        Numero_1 = obtener_cosas_Mayor_que(cadena, 1)
        Numero_2 = obtener_cosas_Mayor_que(cadena, 2)
        Variable_a_asignar = Obtener_variable(cadena , 0)

        if Variable_a_asignar not in Almacen_Variables:
            print("No puedes asignar algo a una variable que no existe")
            return None
        
        if Numero_1 in Almacen_Variables:
            Numero_1 = Almacen_Variables[Numero_1]
        
        if Numero_2 in Almacen_Variables:
            Numero_2 = Almacen_Variables[Numero_2]
        
        Numero_1 = str(Numero_1) if Numero_1 is not None else ""
        Numero_2 = str(Numero_2) if Numero_2 is not None else ""

        if (bool(re.match(Int, Numero_1))) and (bool(re.match(Int, Numero_2))):
            Sumado = int(Numero_1) > int(Numero_2)
            Almacen_Variables[Variable_a_asignar] = Sumado

        else:
            print("Operacion > mal definida")        

    else:
        return print("Operacion Mayor que invalida")

def Realizar_Comaparion_igualdad(cadena):
    '''
    ***
    cadena: string 
    ...
    ***
    No retorna nada, solo hace la suma de los numeros y los guarda en el diccionario
    ***
    Tomo en cuenta todas las posibilidades que puede pasar con la suma y las resuelvo, en caso de ser una suma
    imposible printeo por consola "No se realizo suma, ya que estas sumando una variable que no esta definida"
    '''
    if obtener_cosas_a_comparar(cadena, 1):

        Numero_1 = obtener_cosas_a_comparar(cadena, 1)
        Numero_2 = obtener_cosas_a_comparar(cadena, 2)
        Variable_a_asignar = Obtener_variable(cadena , 0)

        if Variable_a_asignar not in Almacen_Variables:
            print("No puedes asignar algo a una variable que no existe")
            return None
        
        if Numero_1 in Almacen_Variables:
            Numero_1 = Almacen_Variables[Numero_1]
        
        if Numero_2 in Almacen_Variables:
            Numero_2 = Almacen_Variables[Numero_2]
        
        Numero_1 = str(Numero_1) if Numero_1 is not None else ""
        Numero_2 = str(Numero_2) if Numero_2 is not None else ""
     
        if (bool(re.match(Int, Numero_1))) and (bool(re.match(Int, Numero_2))):
            Sumado = int(Numero_1) == int(Numero_2)
            Almacen_Variables[Variable_a_asignar] = Sumado
        
        if (bool(re.match(String, Numero_1))) and (bool(re.match(String, Numero_2))):
            Sumado = Numero_1 == Numero_2
            Almacen_Variables[Variable_a_asignar] = Sumado

        elif ((bool(re.match(String, Numero_1))) and (bool(re.match(Int, Numero_2)))) or ((bool(re.match(Int, Numero_1))) and (bool(re.match(String, Numero_2)))):
            return False

        else:
            print("No se realizo comparacion, ya que estas comparando una variable que no esta definida")        

    else:
        return print("comparacion invalida")    

def MOSTRAR(cadena):
    Variable_a_buscar = Obtener_variable(cadena, 2)
    
    if Variable_a_buscar not in Almacen_Variables:
        print(f"Variable {Variable_a_buscar} no existe")
        return None
    else:
        value = Almacen_Variables[Variable_a_buscar]
        # Abrir el archivo en modo append para no sobrescribir el contenido existente
        with open('archivo.txt', 'a') as archivo:
            archivo.write(value + "\n")
        

def Obtener_tipo_de_dato(cadena):
    '''
    ***
    cadena : Cadena que cumpla con la RegEx Procesamiento_datos 
    ...
    ***
    Retorna el valor del dato que contenga la cadena, dependiendo del tipo de operación
    ***
    '''
    if re.match(Procesamiento_datos, cadena):

        if re.match(ASIG, cadena):
            Asignacion(cadena)

        elif re.match(Suma, cadena):
            Realizar_suma(cadena)

        elif re.match(Multiplicacion, cadena):
            Realizar_multiplicacion(cadena)

        elif re.match(Mayor_que, cadena):
            Realizar_Mayor_que(cadena)

        elif re.match(Igual_que, cadena):
            Realizar_Comaparion_igualdad(cadena)
            ##print("Se pide una comparación de igualdad")

        else:
            print("No se ha detectado una operación válida")

        return None
    
    elif re.match(DEFINE_PATTERN, cadena):
        DEFINE(cadena)

    elif re.match(MOSTRAR_RegEx, cadena):
        MOSTRAR(cadena)
    else:
        print("Error de sintaxis")

def prueba():
    for clave, valor in Almacen_Variables.items():
        print(f"{clave}: {valor}")
        print(type(Almacen_Variables[clave]))
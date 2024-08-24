import re
from RegEx import Int, String, MOSTRAR_RegEx, Procesamiento_datos, ASIG, Suma, Multiplicacion, Mayor_que,  Igual_que, Variable, DEFINE_PATTERN
from Repetitivo import *
from aux_funcion import *
Almacen_Variables = {}

def DEFINE(cadena, i):
    '''
    ***
    cadena : string
    n : int
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
        return True
    else:
        print(f"No se puede reedifinir la variable {Var_para_dic} en la linea {i}")
        return False
        

def Asignacion(cadena, i):
    '''
    ***
    cadena : string
    i : int
    ...
    ***
    Retorna booleanos
    ***
    Esta funcion retorna true o false dependiendo de si hay un error o no el el codigo proporcionado
    controla cada caso en el que podria funcionar o fallar una asignacion
    '''
    Var = Obtener_variable(cadena , 0)
    Info = Obtener_informacion_a_almacenar(cadena)

    if Var not in Almacen_Variables:
        print(f"No puedes asignar un valor a {Var} en la linea {i} ya que no esta definida")
        return True
    
    if (bool(re.match(Variable, Info))):
        if Info not in Almacen_Variables:
            print(f"Operacion ASIG mal definida, ya que {Info} no esta definida. Error en linea {i}")
            return True
        else:
            Auxiliar = Almacen_Variables[Info]
            Almacen_Variables[Var] = Control_tipo_dato(Auxiliar)
            return False

    elif (Info not in Almacen_Variables):
        Almacen_Variables[Var] = Control_tipo_dato(Info)
        return False

def Realizar_suma(cadena, i):
    '''
    ***
    cadena: string 
    i : int
    ...
    ***
    retorna true o none
    ***
    Tomo en cuenta todas las posibilidades que puede pasar con la suma y las resuelvo, en caso de ser una suma
    imposible printeo por consola y retorno True para hacer control de flujo
    '''
    if obtener_cosas_a_Sumar(cadena, 1):

        Numero_1 = obtener_cosas_a_Sumar(cadena, 1)
        Numero_2 = obtener_cosas_a_Sumar(cadena, 2)
        Variable_a_asignar = Obtener_variable(cadena , 0)

        if Variable_a_asignar not in Almacen_Variables:
            print(f"No puedes asignar un valor a la varible {Variable_a_asignar} ya que no esta definida existe. Linea {i}")
            return True
        
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
            print(f"No se realizo suma, ya que estas sumando una variable que no esta definida. linea {i}")        

    else:
        print(f"Suma invalida en {i}")

def Realizar_multiplicacion(cadena,i):
    '''
    ***
    cadena: string 
    i: int
    ...
    ***
    True o None
    ***
    Tomo en cuenta todas las posibilidades que puede pasar con la multiplicacion y las resuelvo, en caso de ser una multiplicacion
    imposible printeo por consola y retorno true para control de flujo
    '''
    if obtener_cosas_a_multiplicar(cadena, 1):
        
        Numero_1 = obtener_cosas_a_multiplicar(cadena, 1)
        Numero_2 = obtener_cosas_a_multiplicar(cadena, 2)
        Variable_a_asignar = Obtener_variable(cadena , 0)

        if Variable_a_asignar not in Almacen_Variables:
            print(f"No puedes asignar un valor a {Variable_a_asignar} que no existe. Linea {i}")
            return True
        
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
            print(f"No se realizo la Multiplicacion, ya que estas multiplicando una variable que no esta definida. Linea {i}") 
            return True       

    else:
        print("Multiplicacion invalida")
        return True

def Realizar_Mayor_que(cadena,i):
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
            print(f"No puedes asignar un valor a {Variable_a_asignar} que no existe. Linea {i}")
            return True
        
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
            print(f"Operacion > mal definida. Linea {i}")   
            return True     

    else:
        print(f"Operacion Mayor que invalida. Linea {i}")
        return True

def Realizar_Comaparion_igualdad(cadena,i):
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
            print(f"No puedes asignar un valor a {Variable_a_asignar} que no existe. Linea {i}")
            return True
        
        if Numero_1 in Almacen_Variables:
            Numero_1 = Almacen_Variables[Numero_1]
        
        if Numero_2 in Almacen_Variables:
            Numero_2 = Almacen_Variables[Numero_2]
        
        Numero_1 = str(Numero_1) if Numero_1 is not None else ""
        Numero_2 = str(Numero_2) if Numero_2 is not None else ""

        if (bool(re.match(Int, Numero_1))) and (bool(re.match(Int, Numero_2))):
            Sumado = int(Numero_1) == int(Numero_2)
            Almacen_Variables[Variable_a_asignar] = Sumado
        
        elif (bool(re.match(String, Numero_1))) and (bool(re.match(String, Numero_2))):
            Sumado = Numero_1 == Numero_2
            Almacen_Variables[Variable_a_asignar] = Sumado

        elif ((bool(re.match(String, Numero_1))) and (bool(re.match(Int, Numero_2)))) or ((bool(re.match(Int, Numero_1))) and (bool(re.match(String, Numero_2)))):
            Almacen_Variables[Variable_a_asignar] = False

        else:
            print(f"No se realizo comparacion, ya que estas comparando una variable que no esta definida. Linea {i}")        

    else:
        print(f"Comparacion invalida {i}")    

def MOSTRAR(cadena, i):
    Variable_a_buscar = Obtener_variable(cadena, 2)
    
    if Variable_a_buscar not in Almacen_Variables:
        print(f"Variable {Variable_a_buscar} no existe")
        return None
    else:
        value = Almacen_Variables[Variable_a_buscar]
        value = str(value)
        # Abrir el archivo en modo append para no sobrescribir el contenido existente
        with open('output.txt', 'a') as archivo:
            archivo.write(value + "\n")
        
def Obtener_tipo_de_dato(cadena, Flag , i):
    '''
    ***
    cadena : Cadena que cumpla con la RegEx Procesamiento_datos 
    Flag : bool
    i = int
    ...
    ***
    Retorna un entero
    ***
    Hace el control de entrada y termina el programa en caso de ser necesario
    y recibe la linea en la que vas
    '''
    if (re.match(Procesamiento_datos, cadena)) and Flag:

        if (re.match(ASIG, cadena)) and Flag:
            Retorno = Asignacion(cadena, i)
            if Retorno:
                return False
            return True

        elif (re.match(Suma, cadena)) and Flag:
            Retorno = Realizar_suma(cadena, i)
            if Retorno:
                return False
            return True

        elif (re.match(Multiplicacion, cadena)) and Flag:
            Retorno = Realizar_multiplicacion(cadena, i)
            if Retorno:
                return False
            return True

        elif (re.match(Mayor_que, cadena)) and Flag:
            Retorno = Realizar_Mayor_que(cadena, i)
            if Retorno:
                return False
            return True

        elif (re.match(Igual_que, cadena)) and Flag:
            Retorno = Realizar_Comaparion_igualdad(cadena, i)
            if Retorno:
                return False
            return True

        else:
            print(f"No se ha detectado una operación válida. Linea {i}")

        ##return None
    
    elif (re.match(DEFINE_PATTERN, cadena)) and Flag:
        Retorno = DEFINE(cadena, i)
        if not Retorno:
            return False

        return True

    elif (re.match(MOSTRAR_RegEx, cadena)) and Flag:
        Retorno = MOSTRAR(cadena, i)
        return True
    else:
        if Flag :
           print(f"Error de sintaxis en la linea: {i}") 

        return False

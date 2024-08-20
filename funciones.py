import re
from RegEx import Int, String, Bool_RegEx, Procesamiento_datos

def Boolenizar(B_S):
    '''
    ***
    B_R : RegEx de los booleanos
    B_S : String a pasar a booleano
    ...
    ***
    Retorna un booleano o imprime por consola "Valor no booleano"
    ***
    Compara el string con true, para que guarde true o false en una variable y lo retorna
    '''
    if re.match(Bool_RegEx, B_S):
        Valor_bool = (B_S == "True")
        return Valor_bool
    else:
        print("Valor no booleano")

def Obtener_tipo_de_dato(cadena):
    '''
    ***
    cadena : Cadena que cumpla con la RegEx Procesamiento_datos 
    ...
    ***
    Retorna el valor del dato que contenga la cadena
    ***
    Usando match con las RegEx definidas en RegEx.py encuentro si el valor buscado
    corresponde a int, string o bool, en caso de ser ninguna retorna bool
    '''
    match = re.match(Procesamiento_datos, cadena)
    if match:
        valor = match.group(1)
        if re.match(Int, valor):
            return "int"
        elif re.match(String, valor):
            return "string"
        elif re.match(Bool_RegEx, valor):
            return "bool"
    return None
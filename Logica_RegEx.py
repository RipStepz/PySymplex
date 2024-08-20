import re
from RegEx import Bool_RegEx

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
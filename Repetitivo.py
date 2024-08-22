from RegEx import Int, String, Variable
import re

def obtener_cosas_a_Sumar(cadena, n):
    '''
    ***
    cadena : string
    n : entero
    ...
    ***
    retorna el primer o segundo valor dependiendo de cual se le pida a la funcion, retorna false en caso
    de no ser un valor esperado
    ***
    Cree una nueva Regex con el objetivo de poder crear dos grupos y extrear los valores
    luego simplemente retorno uno o el otro dependiendo de cual pidan en la funcion, en caso de ser un valor invalido, se retorna false
    '''
    regex_int = r'\+\s*(' + Variable + r'|' + Int + r'|'+ String +r')\s+(' + Variable + r'|' + Int + r'|'+ String + r')'
    match = re.search(regex_int , cadena)

    if match:
    
        valor1 = match.group(1)
        valor1.strip()
        valor2 = match.group(2)
        valor2.strip()
        
        if n == 1:
            return valor1
        elif n == 2:
            return valor2
    
    else:
        return False
    
def obtener_cosas_a_multiplicar(cadena, n):
    '''
    ***
    cadena : string
    n : entero
    ...
    ***
    retorna el primer o segundo valor dependiendo de cual se le pida a la funcion, retorna false en caso
    de no ser un valor esperado
    ***
    Cree una nueva Regex con el objetivo de poder crear dos grupos y extrear los valores
    luego simplemente retorno uno o el otro dependiendo de cual pidan en la funcion, en caso de ser un valor invalido, se retorna false
    '''
    regex_multiplicacion = r'\*\s*(' + Variable + r'|' + Int + r')\s+(' + Variable + r'|' + Int + r')'
    match = re.search(regex_multiplicacion, cadena)

    if match:
        valor1 = match.group(1).strip()
        valor2 = match.group(2).strip()

        if n == 1:
            return valor1
        elif n == 2:
            return valor2
    else:
        return False

def obtener_cosas_Mayor_que(cadena, n):
    '''
    ***
    cadena : string
    n : entero
    ...
    ***
    Retorna el primer o segundo valor dependiendo de cuál se le pida a la función, retorna False en caso
    de no ser un valor esperado.
    ***
    Cree una nueva Regex con el objetivo de crear dos grupos y extraer los valores
    luego simplemente retorno uno o el otro dependiendo de cuál pidan en la función. En caso de ser un valor inválido, se retorna False.
    '''
    regex_comparacion = r'.*>\s*(' + Variable + r'|' + Int + r')\s+(' + Variable + r'|' + Int + r')'
    match = re.search(regex_comparacion, cadena)

    if match:
        valor1 = match.group(1).strip()
        valor2 = match.group(2).strip()
        if n == 1:
            return valor1
        elif n == 2:
            return valor2
    else:
        return False
    
def obtener_cosas_a_comparar(cadena, n):
    '''
    ***
    cadena : string
    n : entero
    ...
    ***
    Retorna el primer o segundo valor dependiendo de cuál se le pida a la función, retorna False en caso
    de no ser un valor esperado.
    ***
    Cree una nueva Regex con el objetivo de crear dos grupos y extraer los valores
    luego simplemente retorno uno o el otro dependiendo de cuál pidan en la función. En caso de ser un valor inválido, se retorna False.
    '''
    regex_comparacion = r'.*==\s*(' + Variable + r'|' + Int + r'|' + String + r')\s+(' + Variable + r'|' + Int + r'|' + String + r')'
    match = re.search(regex_comparacion, cadena)

    if match:
        valor1 = match.group(1).strip()
        valor2 = match.group(2).strip()

        if n == 1:
            return valor1
        elif n == 2:
            return valor2
    else:
        return False
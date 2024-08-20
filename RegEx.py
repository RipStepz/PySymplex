Variable = r'\$_[A-Z]\w*'
DEFINE_PATTERN = r'^\s*DEFINE\s+' + Variable + r'\s*$'

Int = r'\d+'
String = r'#.*#'
Bool_RegEx = r'(True|False)'

ASIG = r'\s*' + Variable + r'\s+ASIG\s+(' + Int + r'|' + String + r'|' + Bool_RegEx + r')\s*$'
Suma = r'\s*' + Int + r'\s+\+' + r'\s+'+ Int + r'\s*$'
Multiplicacion = r'\s*' + Int + r'\s+\*' + r'\s+'+ Int + r'\s*$'
Mayor_que = r'\s*' + Int + r'\s+>\s+ ' + Int + r'\s*$'
Igual_que = r'\s*' + r'(' + Int + r'|' + String + r')\s+==\s+(' + Int + r'|' + String + r')\s*$'

Procesamiento_datos = r'^\s*DP' + ASIG
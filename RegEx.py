import re
Variable = r'.*\$_[A-Z]\w*'

Int = r'\d+'
String = r'#.*#'
Bool_RegEx = r'(True|False)'

DEFINE_PATTERN = r'^\s*DEFINE\s+' + Variable +r'\s*'
ASIG = r'.*\s*' + Variable + r'\s+ASIG\s+(' + Int + r'|' + String + r'|' + Bool_RegEx + r'|' + Variable + r')\s*$'
Suma = r'.*\s*' + r'\+\s*' + r'(' + Variable + r'|' + Int + r'|' + String +  r')\s+' + r'(' + Variable + r'|' + Int + r'|' + String + r')\s*'
Multiplicacion = r'.*\s*' + r'\*\s*' + r'(' + Variable + r'|' + Int +  r')\s+' + r'(' + Variable + r'|' + Int + r')\s*'
Mayor_que = r'.*\s*' + r'>\s*' + r'(' + Variable + r'|' + Int +  r')\s+' + r'(' + Variable + r'|' + Int + r')\s*'
Igual_que = r'.*\s*(' + Variable + r'|' + Int + r'|' + String + r')\s+==\s+(' + Variable + r'|' + Int + r'|' + String + r')\s*'
MOSTRAR_RegEx = r'\s*MOSTRAR\(' + Variable +r'\)\s*$'

Procesamiento_datos = r'^\s*DP\s+' + Variable + r'\s+.*'
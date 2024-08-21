##import re
Variable = r'.*\$_[A-Z]\w*'
DEFINE_PATTERN = r'^\s*DEFINE\s+' + Variable + r'\s*$'

Int = r'\d+'
String = r'#.*#'
Bool_RegEx = r'(True|False)'

ASIG = r'.*\s*' + Variable + r'\s+ASIG\s+(' + Int + r'|' + String + r'|' + Bool_RegEx + r'|' + Variable + r')\s*$'
Suma = r'.*\s*' + r'\+\s*' + r'(' + Variable + r'|' + Int + r'|' + String +  r')\s+' + r'(' + Variable + r'|' + Int + r'|' + String + r')\s*'
Multiplicacion = r'.*\s*' + r'\*\s*' + r'(' + Variable + r'|' + Int +  r')\s+' + r'(' + Variable + r'|' + Int + r')\s*'
Mayor_que = r'.*\s*' + r'>\s*' + r'(' + Variable + r'|' + Int +  r')\s+' + r'(' + Variable + r'|' + Int + r')\s*'
Igual_que = Igual_que = r'.*\s*(' + Variable + r'|' + Int + r'|' + String + r')\s+==\s+(' + Variable + r'|' + Int + r'|' + String + r')\s*$'

Procesamiento_datos = r'^\s*DP\s+' + r'(' + ASIG + r'|' + Suma + r'|' + Multiplicacion + r'|' + Mayor_que + r'|' + Igual_que + r')\s*$'

##print(bool(re.match(Mayor_que,"DP $_Vardest > 5 $_Vardest" )))
##print(bool(re.match(Igual_que,"DP $_Vardest == $_Var2 True")))

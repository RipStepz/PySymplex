import re

ex = re.compile("\d\d\d")

cadena_uno = ex.search("213")
##cadena_dos = ex.search("arturo al2314321monacid").group()
##cadena_tres = ex.search("hsahsak2134sadfsa").group()


if cadena_uno is None:
    print("no existen coincidencias")

else:
    print("Existen coincidencias")
"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = expresiones_regulares
Autor = admin
Fecha creación = 23/10/16
--------------------------
"""

import re
patron_nombre = '[A-Z]{1}[a-z]* [A-Z]{1}[a-z]*'

print(re.search(patron_nombre, 'Víctor'))
print(re.search(patron_nombre, 'VIctor'))
"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = prueba
Autor = admin
Fecha creación = 16/10/16
--------------------------
"""

from estructura_academica.dominio.general.domicilio import *

mi_domicilio = Domicilio('Corrientes',
                          659,
                          '',
                          '',
                          'Paraná',
                          'Entre Ríos',
                          '3100')

otro_domicilio = Domicilio('Moreno',
                          None,
                          '',
                          '',
                          'Paraná',
                          'Entre Ríos',
                          '3100')

print('Los domicilios son iguales:')
if (mi_domicilio == None):
    print('Si')
else:
    print('No')
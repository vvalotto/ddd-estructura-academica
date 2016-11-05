"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = domicilio
Autor = admin
Fecha creación = 16/10/16
--------------------------
"""
from .objeto_valor import *

'''
Value Object: Direccion
'''

class Domicilio(ObjetoValor):

    @property
    def calle(self):
        return self._calle

    @property
    def numero(self):
        return self._numero

    @property
    def piso(self):
        return self._piso

    @property
    def departamento(self):
        return self._departamento

    def __init__(self, calle
                    , numero
                    , piso
                    , departamento):

        self._validar_calle(calle)
        self._validar_numero(numero)
        self._validar_departamento(departamento)
        self._validar_piso(piso)

        self._calle = calle
        self._numero = numero
        self._piso = piso
        self._departamento = departamento

        return

    def __str__(self):
        return self._numero + "\ " + \
               self._calle + "\ " + \
               self._departamento + "\ " + \
               self._piso + "\ "

    def _validar_calle(self):
        return True

    def _validar_numero(self):
        return True

    def _validar_departamento(self):
        return True

    def _validar_piso(self):
        return True


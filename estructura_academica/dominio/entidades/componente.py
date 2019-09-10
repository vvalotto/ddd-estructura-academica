"""
Entidad Componente
"""

from estructura_academica.dominio.base.entidad import *
from estructura_academica.dominio.base.texto_no_vacio import *

TIPO_COMPONENTE = ['Aplicación', 'Librería', 'módulo']

class NombreComponente(TextoNoVacio):

    def __rep__(self):
        return self.texto


class Componente(Entidad):

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        return

    @property
    def tipo_componente(self):
        return self._tipo_componente

    @tipo_componente.setter
    def tipo_componente(self, valor):
        if valor in TIPO_COMPONENTE:
            self._tipo_componente = valor
        else:
            raise Exception("No es un tipo de componente valido")
        return

    def __init__(self,  nombre, tipo_componente):
        super().__init__()
        self._nombre = nombre
        if tipo_componente in TIPO_COMPONENTE:
            self._tipo_componente = tipo_componente
        else:
            raise Exception("No es un tipo de componente valido")
        return

    def __repr__(self):
        return str(self.nombre) + ": " + self._tipo_componente

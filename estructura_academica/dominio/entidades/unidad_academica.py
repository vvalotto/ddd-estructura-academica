"""
Entidad Unidad Academica
"""

from estructura_academica.dominio.base.entidad import *
from estructura_academica.dominio.base.texto_no_vacio import *


class NombreUnidadAcademica(TextoNoVacio):

    def __str__(self):
        return self.texto


class NombreUniversidad(TextoNoVacio):

    def __str__(self):
        return self.texto


class UnidadAcademica(Entidad):

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        return

    @property
    def universidad(self):
        return self._universidad

    @universidad.setter
    def universidad(self, valor):
        self._universidad = valor
        return

    @property
    def domicilio(self):
        return self._domicilio

    @domicilio.setter
    def domicilio(self, valor):
        self._domicilio = valor
        return

    def __init__(self, nombre, universidad, domicilio):
        """
        Construye la entidad
        :param nombre: OV Nombre de la unidad academica
        :param universidad: OV nombre de la universidad
        :param domicilio: OV Domicilio
        """
        super().__init__()
        self._nombre = nombre
        self._universidad = universidad
        self._domicilio = domicilio
        return

    def __repr__(self):
        return str(self.nombre) + " - " + str(self._universidad)

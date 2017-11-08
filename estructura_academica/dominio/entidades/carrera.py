"""
Entidad Carrera
"""

from estructura_academica.dominio.base.entidad import *
from estructura_academica.dominio.base.texto_no_vacio import *
from estructura_academica.dominio.base.validador import *


class NombreCarrera(TextoNoVacio):
    pass


class IdUnidadAcademica(ObjetoValor):

    @property
    def id_unidad_academica(self):
        return self._id_unidad_academica

    def __init__(self, id_unidad_academica):
        self._id_unidad_academica = id_unidad_academica
        return

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._id_unidad_academica]


class CodigoCarrera(ObjetoValor):

    @property
    def codigo(self):
        return self._codigo_carrera

    def __init__(self,codigo_carrera):

        validacion = ValidadorIdCarrera().validar(codigo_carrera)
        if not validacion.valido:
            raise Exception(validacion.resultado)
        self._codigo_carrera = codigo_carrera
        return

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._codigo_carrera]

    def __repr__(self):
        return self._codigo_carrera


class ValidadorIdCarreraNoNulo(BaseValidador):

    def validar(self, codigo_carrera):
        if codigo_carrera is None:
            self._valido = False
            self._resultado = "Error: Es Nulo"
        return self


class ValidadorIdCarreraFormato(BaseValidador):

        def validar(self, codigo_carrera):
            if len(codigo_carrera) != 5:
                self._valido = False
                self._resultado = "Error de Formato"
            return self


class ValidadorIdCarrera(BaseValidador):
    def validar(self, codigo_carrera):
        validacion = ValidadorIdCarreraNoNulo().validar(codigo_carrera)
        self._valido = self._valido and validacion.valido
        self._resultado = self._resultado + validacion.resultado

        validacion = ValidadorIdCarreraFormato().validar(codigo_carrera)
        self._valido = self._valido and validacion.valido
        self._resultado = self._resultado + validacion.resultado

        return self


class Carrera(Entidad):

    @property
    def codigo_carrera(self):
        return self._codigo_carrera

    @property
    def nombre_carrera(self):
        return self._nombre_carrera

    @nombre_carrera.setter
    def nombre_carrera(self, valor):
        self._nombre_carrera = valor
        return

    @property
    def unidad_academica(self):
        return self._unidad_academica

    def __init__(self, codigo_carrera, nombre_carrera, id_unidad_academica):
        super().__init__()
        self._codigo_carrera = codigo_carrera
        self._nombre_carrera = nombre_carrera
        self._unidad_academica = id_unidad_academica
        return

    def __repr__(self):
        return str(self._codigo_carrera) + " : " + str(self._nombre_carrera)
"""
Entidad Materia
"""

from estructura_academica.dominio.base.entidad import *
from estructura_academica.dominio.base.texto_no_vacio import *


class Codigo(ObjetoValor):

    @property
    def codigo(self):
        return self._codigo

    def __init__(self, codigo):

        validacion = ValidadorCodigoMateria().validar(codigo)
        if not validacion.valido:
            raise Exception(validacion.resultado)
        self._codigo = codigo
        return

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._codigo]

    def __str__(self):
        return self._codigo


class ValidadorCodigoMateriaNoNulo(BaseValidador):

    def validar(self, codigo):
        if codigo is None:
            self._valido = False
            self._resultado = "Error: Es Nulo"
        return self


class ValidadorCodigoMateriaFormato(BaseValidador):

        def validar(self, codigo):
            if len(codigo) != 5:
                self._valido = False
                self._resultado = "Error de Formato"
            return self


class ValidadorCodigoMateria(BaseValidador):
    def validar(self, codigo):
        validacion = ValidadorCodigoMateriaNoNulo().validar(codigo)
        self._valido = self._valido and validacion.valido
        self._resultado = self._resultado + validacion.resultado

        validacion = ValidadorCodigoMateriaFormato().validar(codigo)
        self._valido = self._valido and validacion.valido
        self._resultado = self._resultado + validacion.resultado

        return self


class NombreMateria(TextoNoVacio):
    pass


class IdCarrera(ObjetoValor):

    @property
    def id_carrera(self):
        return self._id_carrera

    def __init__(self, id_carrera):
        self._id_carrera = id_carrera
        return

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._id_carrera]


class Materia(Entidad):

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        return

    @property
    def plan(self):
        return self._plan

    @plan.setter
    def plan(self, valor):
        self._plan = valor
        return

    @property
    def id_carrera(self):
        return self._id_carrera

    def __init__(self, codigo, nombre, plan, id_carrera):
        super().__init__()
        self._codigo = codigo
        self._nombre = nombre
        self._plan = plan
        self._id_carrera = id_carrera
        return
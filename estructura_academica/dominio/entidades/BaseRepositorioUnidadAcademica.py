"""
Clase Abstracta que define el repositorio de la Unidad Academica
"""
from .BaseRepositorio import *


class BaseRepositorioUnidadAcademica(BaseRepositorio):

    @abstractmethod
    def guardar(self, unidad_academica):
        pass

    @abstractmethod
    def recuperar(self, id):
        pass

    @abstractmethod
    def validar_existencia(self, criterio):
        pass

    @abstractmethod
    def recuperar_por_nombre(self, nombre):
        pass

    @abstractmethod
    def obtener_todo(self):
        pass

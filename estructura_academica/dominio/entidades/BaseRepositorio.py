"""
Clase Abstracta Repositorio - Define la interfaz más elementla
"""
from abc import *


class BaseRepositorio(metaclass=ABCMeta):

    @abstractmethod
    def guardar(self, entidad):
        pass

    @abstractmethod
    def recuperar(self, id):
        pass

    @abstractmethod
    def obtener_todo(self):
        pass

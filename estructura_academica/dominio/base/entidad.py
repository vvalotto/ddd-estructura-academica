"""
Clase Base Entidad
"""

from abc import abstractmethod, ABCMeta
import uuid


class Entidad(metaclass=ABCMeta):

    @property
    def id(self):
        return self._id

    def __init__(self):
        self._id = uuid.uuid4()
        return

    def __eq__(self, otra_entidad):

        if otra_entidad.id is None:
            raise EntidadSinIdentificacion()

        return self._id == otra_entidad.id


class EntidadSinIdentificacion(Exception):

    def __init__(self):
        print("Error: Entidad Sin Identificacion")
        return


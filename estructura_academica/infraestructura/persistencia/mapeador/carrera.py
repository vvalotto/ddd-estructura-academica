"""

"""
from sqlalchemy import MetaData

from estructura_academica.dominio.entidades.carrera import *
from estructura_academica.infraestructura.persistencia.modelo.base_de_datos import *

class MapeadorDatosCarrera:

    def __init__(self, contexto):
        self._contexto = contexto
        self._entidad = None
        self._dto_base_datos = None
        return

    def dto_a_entidad(self, dto):
        self._dto_base_datos = dto
        nombre_carrera = NombreCarrera(self._dto_base_datos.nombre_carrera)
        codigo_carrera = CodigoCarrera(self._dto_base_datos.codigo_carrera)
        id_unidad_academica = IdUnidadAcademica(self._dto_base_datos.id_unidad_academica)
        self._entidad = Carrera(codigo_carrera, nombre_carrera, id_unidad_academica)
        self._entidad.identificacion = self._dto_base_datos.id
        return self._entidad

    def entidad_a_dto(self, carrera):
        self._entidad = carrera
        self._dto_base_datos = CarreraDTO()
        self._dto_base_datos.metadata = MetaData(bind=self._contexto.recurso)
        self._dto_base_datos.id = carrera.identificacion
        self._dto_base_datos.codigo_carrera = carrera.codigo_carrera.codigo
        self._dto_base_datos.nombre_carrera = carrera.nombre_carrera.texto
        self._dto_base_datos.id_unidad_academica = carrera.unidad_academica.id_unidad_academica
        return self._dto_base_datos

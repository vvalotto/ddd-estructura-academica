"""

"""
from sqlalchemy import MetaData

from estructura_academica.dominio.entidades.unidad_academica import *
from estructura_academica.dominio.general.domicilio import *


class MapeadorDatosUnidadAcademica:

    def __init__(self, contexto):
        self._contexto = contexto
        self._entidad = None
        self._dto_base_datos = None
        return

    def dto_a_entidad(self, dto):
        self._dto_base_datos = dto
        nombre_ua = NombreUnidadAcademica(self._dto_base_datos.nombre_unidad_academica)
        nombre_universidad = NombreUniversidad(self._dto_base_datos.nombre_universidad)
        domicilio = Domicilio(self._dto_base_datos.domicilio_calle,
                              self._dto_base_datos.domicilio_numero,
                              self._dto_base_datos.domicilio_piso,
                              self._dto_base_datos.domicilio_depto)
        self._entidad = UnidadAcademica(nombre_ua, nombre_universidad, domicilio)
        self._entidad.identificacion = self._dto_base_datos.id
        return self._entidad

    def entidad_a_dto(self, unidad_academica):
        self._entidad = unidad_academica
        self._dto_base_datos= UnidadAcademicaDTO()
        self._dto_base_datos.metadata = MetaData(bind=self._contexto.recurso)
        self._dto_base_datos.id = unidad_academica.identificacion
        self._dto_base_datos.nombre_unidad_academica = unidad_academica.nombre.texto
        self._dto_base_datos.nombre_universidad = unidad_academica.universidad.texto
        self._dto_base_datos.domicilio_calle = unidad_academica.domicilio.calle
        self._dto_base_datos.domicilio_numero = unidad_academica.domicilio.numero
        self._dto_base_datos.domicilio_piso = unidad_academica.domicilio.piso
        self._dto_base_datos.domicilio_depto = unidad_academica.domicilio.departamento
        return self._dto_base_datos

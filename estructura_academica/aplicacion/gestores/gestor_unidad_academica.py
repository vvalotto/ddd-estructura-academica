"""
Servicio de Aplicacion que gestiona el tratamiento de las unidades academicas
"""
from estructura_academica.dominio.entidades.unidad_academica import *
from estructura_academica.dominio.general.domicilio import *


class GestorUnidadAcademica:
    """
    Clase de aplicación que es la responsable de realizar la
    administración de la entidad Unidad Academica.
    Basicamente maneja los CRUD de la entidad, no tiene otra
    responsabilidad
    """
    def __init__(self):
        self._unidad_academica = None
        self._repositorio = None
        return

    def crear_unidad_academica(self, nombre_unidad,
                               nombre_universidad,
                               domicilio):
        """
        Metodo Factoria que crea una nueva entidad
        :param nombre_unidad: nombre de la unidad academica (OV)
        :param nombre_universidad: nombre de la universidad (OV)
        :param domicilio:
        :return: la unidad academica creada
        """
        self._unidad_academica = UnidadAcademica(nombre_unidad,
                                                 nombre_universidad,
                                                 domicilio)
        return self._unidad_academica

    def asignar_repositorio(self, repositorio):
        """
        Asocia el repositorio donde se persisten las entidades
        :param repositorio:
        :return:
        """
        self._repositorio = repositorio
        return

    def guardar_unidad_academica(self):
        self._repositorio.guardar(self._unidad_academica)

    def recuperar_unidad_academica_por_nombre(self, nombre):
        dto = self._repositorio.recuperar_por_nombre(nombre)
        self._unidad_academica = self._mapear_DTO_a_unidad_academica(dto)
        return self._unidad_academica

    def recuperar_unidad_academica(self, id_unidad_academica):
        dto = self._repositorio.recuperar(id_unidad_academica)
        self._unidad_academica = self._mapear_DTO_a_unidad_academica(dto)
        return self._unidad_academica

    def obtener_todas_las_unidades_academicas(self):
        lista_unidad_academica = []
        for ua in list(self._repositorio.obtener_todas()):
            lista_unidad_academica.append(self._mapear_DTO_a_unidad_academica(ua))
        return lista_unidad_academica

    def existe_unidad_academica(self, nombre):
        return self._repositorio.validar_exitencia(nombre)

    def _mapear_DTO_a_unidad_academica(self, dto_unidad_academica):
        nombre = NombreUnidadAcademica(dto_unidad_academica.nombre_unidad_academica)
        universidad = NombreUniversidad(dto_unidad_academica.nombre_universidad)
        domicilio = Domicilio(dto_unidad_academica.domicilio_calle,
                              dto_unidad_academica.domicilio_numero,
                              dto_unidad_academica.domicilio_piso,
                              dto_unidad_academica.domicilio_depto)

        return UnidadAcademica(nombre, universidad, domicilio)

    def _mapear_unidad_academica_a_DTO(self):
        pass

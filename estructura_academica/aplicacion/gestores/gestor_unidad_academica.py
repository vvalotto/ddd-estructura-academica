"""
Servicio de Aplicacion que gestiona el tratamiento de las unidades academicas
"""
from sqlalchemy.orm import sessionmaker

from estructura_academica.dominio.entidades.unidad_academica import *


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
        self._nuevo = False
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
        self._nuevo = True
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
        self._abrir_unidad_de_trabajo()
        if self._nuevo:
            try:
                self._repositorio.agregar(self._unidad_academica)
            except Exception():
                print('Error al guardar')
        else:
            try:
                self._repositorio.actualizar(self._unidad_academica)
            except Exception():
                print('Error al guardar')
        self._cerrar_unidad_de_trabajo()
        self._nuevo = False
        return

    def recuperar_unidad_academica_por_nombre(self, nombre):
        self._abrir_unidad_de_trabajo()
        self._unidad_academica = self._repositorio.recuperar_por_nombre(nombre)
        self._cerrar_unidad_de_trabajo()
        return self._unidad_academica

    def recuperar_unidad_academica(self, id_unidad_academica):
        self._abrir_unidad_de_trabajo()
        """
        dto = self._repositorio.recuperar(id_unidad_academica)
        self._unidad_academica = self._mapear_DTO_a_unidad_academica(dto)
        """
        self._unidad_academica = self._repositorio.recuperar(id_unidad_academica)
        self._cerrar_unidad_de_trabajo()
        return self._unidad_academica

    def obtener_todas_las_unidades_academicas(self):
        self._abrir_unidad_de_trabajo()
        lista_unidad_academica = self._repositorio.obtener_todo()
        """
        for ua in list(self._repositorio.obtener_todo()):
            lista_unidad_academica.append(self._mapear_DTO_a_unidad_academica(ua))
        """
        self._cerrar_unidad_de_trabajo()
        return lista_unidad_academica

    def existe_unidad_academica(self, nombre):
        self._abrir_unidad_de_trabajo()
        valida = self._repositorio.validar_existencia(nombre)
        self._cerrar_unidad_de_trabajo()
        return valida

    def _abrir_unidad_de_trabajo(self):
        sesion = sessionmaker(bind=self._repositorio.contexto.recurso)
        self._repositorio.contexto.sesion = sesion()
        return

    def _cerrar_unidad_de_trabajo(self):
        self._repositorio.contexto.sesion.commit()
        return

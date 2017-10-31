"""
Se implementa el repositorio de la Unidad Academica en Base de Datos
"""
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker, Session
from estructura_academica.dominio.entidades.BaseRepositorioUnidadAcademica import *
from estructura_academica.infraestructura.persistencia.modelo.base_de_datos import *


class DBRepositorioUnidadAcademica(BaseRepositorioUnidadAcademica):

    def __init__(self, contexto):
        self._contexto = contexto
        return

    def guardar(self, unidad_academica):
        try:
            Session = sessionmaker(bind=self._contexto.recurso)
            sesion = Session()
            sesion.add(self._mapear_a_tabla(unidad_academica))
            sesion.commit()
        except Exception("Error al guardar"):
            print("Repositorio de Unidad Academica")
        return

    def _mapear_a_tabla(self, unidad_academica):
        ua = UnidadAcademicaDTO()
        ua.metadata = MetaData(bind=self._contexto.recurso)
        ua.id = str(unidad_academica.id)
        ua.nombre_unidad_academica = unidad_academica.nombre.texto
        ua.nombre_universidad = unidad_academica.universidad.texto
        ua.domicilio_calle = unidad_academica.domicilio.calle
        ua.domicilio_numero = unidad_academica.domicilio.numero
        ua.domicilio_piso = unidad_academica.domicilio.piso
        ua.domicilio_depto = unidad_academica.domicilio.departamento
        return ua

    def recuperar(self, id):
        try:
            Session = sessionmaker(bind=self._contexto.recurso)
            sesion = Session()
            unidad_academica = sesion.query(UnidadAcademicaDTO).\
                get(str(id))
            sesion.commit()
        except Exception("Error al recuperar"):
            unidad_academica = None
            print("Repositorio de Unidad Academica")
        return unidad_academica

    def recuperar_por_nombre(self, nombre):
        try:
            Session = sessionmaker(bind=self._contexto.recurso)
            sesion = Session()
            unidad_academica = sesion.query(UnidadAcademicaDTO).\
                filter(UnidadAcademicaDTO.nombre_unidad_academica == nombre)[0]
            sesion.commit()
        except Exception("Error al recuperar"):
            unidad_academica = None
            print("Repositorio de Unidad Academica")
        return unidad_academica

    def validar_existencia(self, nombre):
        try:
            Session = sessionmaker(bind=self._contexto.recurso)
            sesion = Session()
            if len(list(sesion.query(UnidadAcademicaDTO).\
                filter(UnidadAcademicaDTO.nombre_unidad_academica == nombre))) > 0:
                sesion.commit()
                return True
            else:
                return False
        except Exception("Error al recuperar"):
            print("Repositorio de Unidad Academica")
            return False

    def obtener_todo(self):
        try:
            Session = sessionmaker(bind=self._contexto.recurso)
            sesion = Session()
            lista_unidades_academicas = sesion.query(UnidadAcademicaDTO).all()
            sesion.commit()
            return lista_unidades_academicas
        except Exception("Error al recuperar"):
            print("Repositorio de Unidad Academica")
            return None
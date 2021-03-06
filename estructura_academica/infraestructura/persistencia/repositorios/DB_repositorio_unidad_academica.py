"""
Se implementa el repositorio de la Unidad Academica en Base de Datos
"""
from estructura_academica.dominio.entidades.base_repositorio_unidad_academica import *
from estructura_academica.infraestructura.persistencia.modelo.base_de_datos import *


class DBRepositorioUnidadAcademica(BaseRepositorioUnidadAcademica):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        return

    def agregar(self, unidad_academica):
        try:
            sesion = self.contexto.sesion
            sesion.add(self._mapeador.entidad_a_dto(unidad_academica))
        except Exception("Error al guardar"):
            print("Repositorio de Unidad Academica")
        return

    def actualizar(self, unidad_academica):
        """
        Para actualizar la entidad persistida, se pasa la entidad modificada y:
            se mapea la entidad a la estructura de tabla
            se recupera la entidad existente por el id
            se copia la estructura mapeada a la recuperada
            se comitea
        :param unidad_academica:
        :return:
        """
        try:
            sesion = self.contexto.sesion
            unidad_academica_modificada = self._mapeador.entidad_a_dto(unidad_academica)
            unidad_academica_recuperada = sesion.query(UnidadAcademicaDTO).get(unidad_academica.identificacion)
            self._copiar_registro(unidad_academica_modificada, unidad_academica_recuperada)
        except Exception("Error al actualizar"):
            print("Repositorio de Unidad Academica")
        return

    def recuperar(self, identificacion):
        try:
            sesion = self.contexto.sesion
            unidad_academica_dto = sesion.query(UnidadAcademicaDTO).get(identificacion)
            unidad_academica = self._mapeador.dto_a_entidad(unidad_academica_dto)
        except Exception("Error al recuperar"):
            unidad_academica = None
            print("Repositorio de Unidad Academica")
        return unidad_academica

    def recuperar_por_nombre(self, nombre):
        try:
            sesion = self.contexto.sesion
            unidad_academica_dto = sesion.query(UnidadAcademicaDTO).\
                filter(UnidadAcademicaDTO.nombre_unidad_academica == nombre)[0]
            unidad_academica = self._mapeador.dto_a_entidad(unidad_academica_dto)
        except Exception("Error al recuperar"):
            unidad_academica = None
            print("Repositorio de Unidad Academica")
        return unidad_academica

    def validar_existencia(self, nombre):
        try:
            sesion = self.contexto.sesion
            if len(list(sesion.query(UnidadAcademicaDTO).
                                filter(UnidadAcademicaDTO.nombre_unidad_academica == nombre))) > 0:
                return True
            else:
                return False
        except Exception("Error al recuperar"):
            print("Repositorio de Unidad Academica")
            return False

    def obtener_todo(self):
        try:
            lista_unidades_academicas = []
            sesion = self.contexto.sesion
            for ua_dto in sesion.query(UnidadAcademicaDTO).all():
                ua = self._mapeador.dto_a_entidad(ua_dto)
                lista_unidades_academicas.append(ua)
            return lista_unidades_academicas
        except Exception("Error al recuperar"):
            print("Repositorio de Unidad Academica")
            return None

    def _copiar_registro(self, desde, hacia):
        hacia.nombre_unidad_academica = desde.nombre_unidad_academica
        hacia.nombre_universidad = desde.nombre_universidad
        hacia.domicilio_calle = desde.domicilio_calle
        hacia.domicilio_numero = desde.domicilio_numero
        hacia.domicilio_piso = desde.domicilio_piso
        hacia.domicilio_depto = desde.domicilio_depto
        return
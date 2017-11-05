"""
Se implementa el repositorio de la Unidad Academica en Base de Datos
"""
from estructura_academica.dominio.entidades.base_repositorio_carrera import *
from estructura_academica.infraestructura.persistencia.modelo.base_de_datos import *


class DBRepositorioCarrera(BaseRepositorioCarrera):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        return

    def agregar(self, carrera):
        try:
            sesion = self.contexto.sesion
            c = self._mapeador.entidad_a_dto(carrera)
            sesion.add(c)
        except Exception("Error al guardar"):
            print("Repositorio de Unidad Academica")
        return

    def actualizar(self, carrera):
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
            carrera_modificada = self._mapeador.entidad_a_dto(carrera)
            carrera_recuperada = sesion.query(CarreraDTO).get(carrera.identificacion)
            self._copiar_registro(carrera_modificada, carrera_recuperada)
        except Exception("Error al actualizar"):
            print("Repositorio de Unidad Academica")
        return

    def recuperar(self, identificacion):
        try:
            sesion = self.contexto.sesion
            carrera_dto = sesion.query(CarreraDTO).get(identificacion)
            carrera = self._mapeador.dto_a_entidad(carrera_dto)
        except Exception("Error al recuperar"):
            carrera = None
            print("Repositorio de Unidad Academica")
        return carrera

    def recuperar_por_nombre(self, nombre):
        try:
            sesion = self.contexto.sesion
            carrera_dto = sesion.query(CarreraDTO).\
                filter(CarreraDTO.nombre_carrera == nombre)[0]
            carrera = self._mapeador.dto_a_entidad(carrera_dto)
        except Exception("Error al recuperar"):
            carrera = None
            print("Repositorio de Unidad Academica")
        return carrera

    def validar_existencia(self, nombre):
        try:
            sesion = self.contexto.sesion
            if len(list(sesion.query(CarreraDTO).
                                filter(UnidadAcademicaDTO.nombre_unidad_academica == nombre))) > 0:
                return True
            else:
                return False
        except Exception("Error al recuperar"):
            print("Repositorio de Unidad Academica")
            return False

    def obtener_todo(self):
        try:
            lista_carreras = []
            sesion = self.contexto.sesion
            for carrera_dto in sesion.query(UnidadAcademicaDTO).all():
                carrera = self._mapeador.dto_a_entidad(carrera_dto)
                lista_carreras.append(carrera)
            return lista_carreras
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
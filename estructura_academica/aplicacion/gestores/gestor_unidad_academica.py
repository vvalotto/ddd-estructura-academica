"""
Servicio de Aplicacion que gestiona el tratamiento de las unidades academicas
"""
from estructura_academica.dominio.entidades.unidad_academica import *

class GestorUnidadAcademica:

    def __init__(self, repositorio):
        self._unidad_academica = None
        self._repositorio = repositorio
        return

    def crear_unidad_academica(self, nombre_unidad,
                               nombre_universidad,
                               domicilio):
        self._unidad_academica = UnidadAcademica(nombre_unidad,
                                                 nombre_universidad,
                                                 domicilio)
        return

    def guardar_unidad_academica(self):
        pass

    def recuperar_unidad_academica_por_nombre(self):
        pass

    def recuperar_unidad_academica(self):
        pass




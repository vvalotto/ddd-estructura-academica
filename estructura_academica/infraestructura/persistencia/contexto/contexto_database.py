"""
Definición del mecanismo de persistencia (Tecnología para almacenar los datos)
"""
import pymysql

from sqlalchemy import create_engine
from estructura_academica.infraestructura.persistencia.modelo.base_de_datos import *
from estructura_academica.infraestructura.persistencia.contexto.contexto import *


class ContextoDB(BaseContexto):
    """
    Implementa un contexto correspodiente a un motor de base de datos
    """

    @property
    def recurso(self):
        return self._recurso

    def __init__(self, recurso):
        """
        :param recurso:El recurso corresponde al nombre y motor de la base de datos
        :return:
        """
        super().__init__(recurso)
        self._recurso = create_engine(recurso)
        self._recurso.echo = False

    def inicializar_tablas(self):
        """
        Crear las tablas
        :return:
        """
        Base.metadata.bind = self._recurso
        Base.metadata.create_all()


class ContextDBMySQL(ContextoDB):
    """
    Contexto que se especializa en la conexión con MySQL
    """
    def __init__(self, recurso):
        pymysql.install_as_MySQLdb()
        super().__init__(recurso)
        return

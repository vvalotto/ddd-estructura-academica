"""
Definición del Repositorio Base para tratar entidades en Base de Datos
"""
from sqlalchemy.orm import sessionmaker
from dominio.repositorios.core import BaseRepositorio
from abc import ABCMeta

class RepositorioDB(BaseRepositorio):
    """
    Definicion del Repositorio generico para motor de base de datos
    """

    def guardar(self, entidad):
        """
        Persiste la entidad
        :return:
        """
        try:
            if entidad.id is None: #Si la entidad no tiene ID es nueva
                self._persistidor.sesion.add(entidad)
            self._persistidor.sesion.flush()
            self._persistidor.sesion.commit()
        except Exception as ex:
            raise ex
        return

    def obtener_por_id(self, id_entidad):
        """
        Recupera un entidad por su Id
        :return:
        """
        try:
            print(self._entidad)
            entidad = self._persistidor.sesion.query(self._entidad).get(id_entidad)
            print(type(entidad))
            return entidad
        except Exception:
            raise Exception
        return None

    def actualizar(self, entidad):
        try:
            entidad_ant = self._persistidor.sesion.query(self._entidad).get(entidad.id)
            print(entidad_ant)
            entidad_ant = entidad
            print(entidad_ant)
            self._persistidor.sesion.commit()
        except Exception as ex:
            raise ex.args

    def obtener_todos(self):
        """
        Rescata todas las ocurrencias (filas) de la entidad
        :return:
        """
        try:
            lista_entidades = self._persistidor.sesion.query(self._entidad).all()
            return lista_entidades
        except Exception:
            raise Exception
        return None


class NoDuplicable(metaclass=ABCMeta):

    def validar_no_existente(self):
        pass
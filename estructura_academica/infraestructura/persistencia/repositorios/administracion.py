from sqlalchemy.orm import sessionmaker
from infraestructura.persistencia.repositorios.core import *
from dominio.entidades.administracion import *


class DBRepositorioCarrera(RepositorioDB, NoDuplicable):
    '''

    '''
    def validar_no_existente(self, carrera):
        q = self._persistidor.sesion.query(self._entidad).\
            filter(self._entidad.a_nombre == carrera.nombre,
                   self._entidad.a_institucion == carrera.institucion)
        q = self._persistidor.sesion.query(q.exists())
        return not list(q)[0]


class DBRepositorioMateria(RepositorioDB, NoDuplicable):

    def validar_no_existente(self):
        pass

class DBRepositorioRol(RepositorioDB, NoDuplicable):

    def validar_no_existente(self):
        pass


class DBRepositorioUsuario(RepositorioDB):

    def asignar_rol(self, usuario, rol):
        try:
            self._persistidor.sesion.commit()
        except Exception as ex:
            raise ex.args


class DBRepositorioDocente(RepositorioDB):

    def asignar_materia(self, docente, materia):
        pass

    def desasignar_materia(self, docente, materia):
        pass


class DBRepositorioAlumno(RepositorioDB):

    def asignar_materia(self, docente, materia):
        pass

    def actualizar(self, entidad):
        pass

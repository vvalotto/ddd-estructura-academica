"""
Definición del modelo de Datos
"""

from sqlalchemy import Table, Column, Integer, String, ForeignKey


class Database(object):

    def __init__(self, metadata):
        '''
        Define los objetos tabla
        :return:
        '''
        self.unidad_academica = Table('td_unidad_academica', metadata,
                                      Column('id', ))


        self.carrera = Table('td_carrera', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('a_nombre', String(50)),
                            Column('a_institucion', String(50)),
                            Column('a_plan', String(10)),
                            Column('a_habilitado', Integer))

        self.materia = Table('td_materia', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('id_carrera', Integer, ForeignKey('td_carrera.id')),
                            Column('a_nombre', String(50)),
                            Column('a_habilitado', Integer))

        return
"""
Definición del modelo de datos y declaración de las tablas del modelo
"""
from uuid import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class ComponenteDTO(Base):
    """
    Tabla Componente
    """
    __tablename__ = "td_componente"

    id = Column(String(36), primary_key=True)
    nombre_componente = Column(String(200), nullable=False)
    tipo_componente = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Aplicacion (nombre='%s', universidad='%s'>"\
            % (self.nombre_componente)


class ProyectoDTO(Base):
    """
    Tabla Proyecto, relacionada con Aplicacion
    """
    __tablename__ = "td_proyecto"

    id = Column(String(36), primary_key=True)
    nombre_proyecto = Column(String(100), nullable=False)
    descripcion = Column(String(200), nullable=False)
    fecha_fin = Column(String(10), nullable=False)
    id_componente= Column(String(36), ForeignKey(ComponenteDTO.id))

class ElementoDTO(Base):

    __tablename__ = "td_elemento"
    '''
    tipo_elemento
    nombre_elemento
    descripcion_elemento
    relacion con componente
    '''
    id = Column(String(36), primary_key=True)


class DimensionElementoDTO(Base):

    __tablename__ = "td_dimension_elemento"
    '''
    tipo_dimension
    valor_dimension_estimado
    valor_dimension_final
    relacion con elemento
    '''
    id = Column(String(36), primary_key=True)

class EsfuerzoElementoDTO(Base):

    __tablename__ = "td_esfuerzo_elemento"

    '''
    tipo_actividad
    esfuerzo_actividad
    relacion con elemento
    '''
    id = Column(String(36), primary_key=True)


class DefectoElementoDTO(Base):

    __tablename__ = "td_defecto_elemento"
    '''
    fase_defecto
    cantidad_defecto
    relacion con elemento
    '''
    id = Column(String(36), primary_key=True)

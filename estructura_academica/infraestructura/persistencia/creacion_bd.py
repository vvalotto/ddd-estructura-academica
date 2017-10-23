from sqlalchemy import MetaData
from infraestructura.persistencia.contexto.contexto_database import *
from infraestructura.persistencia.repositorios.administracion import *
from aplicacion.managers.core import *
from dominio.entidades.administracion import *

DBEvaluacion = ContextoDB('sqlite:///pysea.sqlite')

DBEvaluacion.inicializar_tablas()
metadata = MetaData(DBEvaluacion._recurso)
DBEvaluacion._recurso.echo = True
metadata.create_all()
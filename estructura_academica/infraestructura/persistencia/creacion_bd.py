#Crea el contexto con el motor sqlite y base de datos
from estructura_academica.infraestructura.persistencia.contexto.contexto_database_sqlite import *

DBEvaluacion = ContextoDBSQLite('sqlite:///proyectos.db')

#Crea la tablas
DBEvaluacion.inicializar_tablas()


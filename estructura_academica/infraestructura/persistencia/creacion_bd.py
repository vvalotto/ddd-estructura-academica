#Crea el contexto con el motor mysql y base de datos
from estructura_academica.infraestructura.persistencia.contexto.contexto_database_sqlite import *
DBEvaluacion = ContextoDB('sqlite:///academica,db')

#Crea la tablas
DBEvaluacion.inicializar_tablas()


from estructura_academica.infraestructura.persistencia.contexto.contexto_database import *

DBEvaluacion = ContextoDB('mysql+pymysql://pysea_admin:pysea@localhost:3306/pysea')

DBEvaluacion.inicializar_tablas()


#Crea el contexto con el motor mysql y base de datos
DBEvaluacion = ContextoDB('mysql+pymysql://pysea_admin:pysea@localhost:3306/pysea')

#Crea la tablas
DBEvaluacion.inicializar_tablas()


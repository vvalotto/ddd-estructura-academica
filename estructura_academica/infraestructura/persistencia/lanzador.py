"""

"""
from sqlalchemy import create_engine
from estructura_academica.infraestructura.persistencia.modelo.base_de_datos import *
from estructura_academica.infraestructura.persistencia.contexto.contexto_database import *
from estructura_academica.aplicacion.gestores.gestor_unidad_academica import *
from estructura_academica.dominio.general.domicilio import *
from estructura_academica.dominio.entidades.unidad_academica import *
from estructura_academica.infraestructura.persistencia.repositorios.DB_repositorio_unidad_academica import *


gestor = GestorUnidadAcademica()
mi_contexto = ContextDBMySQL('mysql+pymysql://pysea_admin:pysea@localhost:3306/pysea')

mi_domicilio = Domicilio('Ruta 10', 'Km 11', ' ', ' ')
mi_nombre_ua = NombreUnidadAcademica('FRP')
mi_universidad = NombreUniversidad('UTN')

mi_unidad_academica = gestor.crear_unidad_academica(mi_nombre_ua, mi_universidad, mi_domicilio)
mi_repositorio = DBRepositorioUnidadAcademica(mi_contexto)

print(mi_unidad_academica)

gestor.asignar_repositorio(mi_repositorio)
gestor.guardar_unidad_academica()

print(mi_repositorio.validar_existencia('FCYT'))

for unidad in mi_repositorio.obtener_todo():
    print(unidad)

print(gestor.recuperar_unidad_academica(mi_unidad_academica.id))



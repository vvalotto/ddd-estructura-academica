from estructura_academica.dominio.entidades.unidad_academica import *
from estructura_academica.dominio.entidades.carrera import *
from estructura_academica.dominio.entidades.materia import *
from estructura_academica.dominio.general.domicilio import *

mi_calle = Calle("Corrientes")
print(mi_calle)

mi_numero = Numero("659")
print(mi_numero)

mi_piso = Piso()
print(mi_piso)

mi_depto = Departamento()
print(mi_depto)

mi_domicilio = Domicilio(mi_calle, mi_numero, mi_piso, mi_depto)
print(mi_domicilio)

facultad = NombreUnidadAcademica("Facultad de Ingenieria")
universidad = NombreUniversidad("UNER")

unidad = UnidadAcademica(facultad, universidad, mi_domicilio)

print(unidad.id)

print(unidad)



carrera = Carrera(CodigoCarrera("ING01"), NombreCarrera("Biongenieria"), unidad.id)

print(carrera.codigo_carrera)
print(carrera.nombre_carrera)
print(carrera.unidad_academica)
print(carrera.id)


materia = Materia(Codigo("BI106"), NombreMateria("Ing de Software"), "Plan 2013", carrera.id)

print(materia.codigo)
print(materia.nombre)
print(materia.plan)
print(materia.id_carrera)
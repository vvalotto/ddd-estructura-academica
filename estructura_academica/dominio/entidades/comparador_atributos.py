"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = comparador_atributos
Autor = admin
Fecha creación = 16/10/16
--------------------------
"""


class ComparadorAtributos():

    @staticmethod
    def comparar_igualdad(atributo_derecha, atributo_izquierda):
        comparacion = True
        if atributo_derecha != atributo_izquierda:
            comparacion = False
        return comparacion
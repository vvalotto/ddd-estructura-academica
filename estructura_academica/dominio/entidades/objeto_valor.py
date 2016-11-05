"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = objeto_valor
Autor = admin
Fecha creación = 22/10/16
--------------------------
"""


tipos_primitivos = ['int', 'str', 'bool', 'float']


class ObjetoValor():

    def obtener_atributos(self):
        for clave, valor in self.__dict__.items():
            if self.__dict__[clave].__class__.__name__ in tipos_primitivos:
                print(clave, '->', valor)
            else:
                self.__dict__[clave].obtener_atributos()
        return

    def __eq__(self, otro):
        for clave, valor in self.__dict__.items():
            if self.__dict__[clave].__class__.__name__ in tipos_primitivos:
                if valor != otro.__dict__[clave] or\
                   self.__dict__[clave].__class__.__name__ != otro.__dict__[clave].__class__.__name__:
                    return False
            else:
                if valor != otro.__dict__[clave]:
                    return False
        return True

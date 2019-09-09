"""
Definición del mecanismo de persistencia (Tecnología para almacenar los datos)
"""

from sqlalchemy import create_engine
from .contexto_database import *

class ContextoDBMySQL(ContextoDB):
    """
    Contexto que se especializa en la conexión con SQlite
    """

    def __init__(self, recurso):
        super().__init__(recurso)
        return

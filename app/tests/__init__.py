import unittest
from app.routes.common import app
#from app.persistencia.diccionario import insertarPersona, personas
#from app.persistencia.lista import insertarPersona, borrarPersonas
from app.persistencia.SQLite import insertarPersona, borrarPersonas

class BaseTestClass(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

        insertarPersona('Pili',44)
        insertarPersona('Hugo',40)

    def tearDown(self):
        borrarPersonas()
        
        



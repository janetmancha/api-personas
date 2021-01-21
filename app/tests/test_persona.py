from . import BaseTestClass
from app.routes import listarPersonas 
import json 
from flask import jsonify


class TestEndPointPersona (BaseTestClass):
    
    def test_listar(self):
        res = self.client.get('/personas')
        self.assertEqual(200, res.status_code)

        resDict = json.loads(res.data) #convertir un json en diccionario o a una lista de python
        #print(resDict)
       
        #comprobar si hugo y pili están en el diccionario creado
        #CON LISTAS
        assert({'edad': 40, 'nombre': 'Hugo'} in resDict)
        assert({'edad': 44, 'nombre': 'Pili'} in resDict)

        #CON DICCIONARIOS
        # assert("Hugo" in resDict)
        # assert(resDict["Hugo"]["edad"],40)
        
        # assert("Pili" in resDict)
        # assert(resDict["Pili"]["edad"],44)

        #comprobar que el diccionario tiene solo dos elementos
        self.assertEqual(len(resDict),2)

    def test_buscarPersona(self):
        res = self.client.get('/personas/Pili')
        self.assertEqual(200, res.status_code)

        res = self.client.get('/personas/janet')
        self.assertEqual(404, res.status_code)
    
    def test_nuevaPersona(self):
        res = self.client.post('/nueva-persona',json={"nombre": "german", "edad": 40})
        self.assertEqual(201, res.status_code)
        
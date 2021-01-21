from flask import Flask, request, jsonify
#from ..persistencia.diccionario import buscarPersona
#from ..persistencia.lista import buscarPersona
from ..persistencia.SQLite import buscarPersona
from app.routes.common import app

@app.route("/personas/<nombre>", methods=['GET']) 
def buscar_persona(nombre):
    result = buscarPersona(nombre)
  
    if result != None:
        return result
    return { "message": "No encontrado" }, 404

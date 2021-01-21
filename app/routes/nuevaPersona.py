from flask import Flask, request, jsonify
#from ..persistencia.diccionario import personas, insertarPersona
#from ..persistencia.lista import insertarPersona
from ..persistencia.SQLite import insertarPersona
from app.routes.common import app


@app.route("/nueva-persona", methods=['POST']) 
def nueva_persona():
    global personas
    data = request.get_json()
    print(data)
    insertarPersona(data["nombre"],data["edad"])
    return { "nombre": data["nombre"]}, 201
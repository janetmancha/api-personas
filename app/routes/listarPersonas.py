from flask import Flask, request, jsonify
#from ..persistencia.diccionario import listarPersonas
#from ..persistencia.lista import listarPersonas
from ..persistencia.SQLite import listarPersonas
from app.routes.common import app

@app.route("/personas", methods=['GET']) 
def listar_persona():
    return jsonify(listarPersonas())
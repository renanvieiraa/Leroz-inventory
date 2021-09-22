from collections import defaultdict
import flask
from flask import json
from flask.json import JSONDecoder, JSONEncoder, jsonify
from flask.wrappers import Response
from flask_cors.decorator import cross_origin
from pymongo import MongoClient
from flask import Flask, Request, jsonify
from flask_cors import CORS
# from werkzeug.wrappers import request
import requests

# //Importação das classes
import auth

cliente = MongoClient('mongodb://localhost:27017')

app = Flask(__name__)
CORS(app)
db = cliente.lerozdb
colecao = db.users

# def setType(contentRequest='ok',type='application/json'):
#     r = Response(contentRequest)
#     r.mimetype = type
#     return r


@app.route('/')
def index():
    return 'index page'

@app.route('/users',methods=['GET','POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def usuarios():
    
    # print(r.headers['content-type'])
    # r.headers['content-type'] = 'application/json'

    obj = colecao.find({"nome": "Administrador"})
    result = []


    for x in obj:
        result.append(x)

    
    return auth.setType(json.dumps(result, default=str))

@app.route('/users/<page_name>', methods=['GET'])
def usuario(page_name):
    pageName = page_name
    obj = colecao.find({"email": page_name})
    result = []
    for x in obj:
        result.append(x)
    return json.dumps(result, default=str)

# print(colecao.find_one())

@app.route('/teste')
def rotaTeste():

    res = Response(response="Teste ok", status=200)
    # res.mimetype = 'teste/teste'


    # res.headers['content-type'] = "application/json"
    
    return res
    # return json.dump(colecao.find())
    

# Mantém o servidor rodando
if __name__ == "__main__":
    app.run(debug=True)
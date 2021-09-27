from collections import defaultdict
from os import error
from re import X
from typing import Mapping
import flask
from flask import json
from flask.json import JSONDecoder, JSONEncoder, jsonify
from flask.wrappers import Response
from flask_cors.decorator import cross_origin
from pymongo import MongoClient
from flask import Flask, Request, jsonify, request
from flask_cors import CORS
# from werkzeug.wrappers import request
# from werkzeug.wrappers import request
# import requests

# //Importação das classes
from auth import Auth

cliente = MongoClient('mongodb://localhost:27017')

app = Flask(__name__)
CORS(app)
db = cliente.lerozdb
colecao = db.users

# def returnRequest(contentRequest='ok',type='application/json'):
#     r = Response(contentRequest)
#     r.mimetype = type
#     return r


@app.route('/',methods=['GET','POST'])
def index():
    respon = Response('teste')
    respon.headers['teste'] = 'pqp porra funciona'
    return respon

@app.route('/users',methods=['GET','POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def usuarios():
    
    # print(r.headers['content-type'])
    # r.headers['content-type'] = 'application/json'

    obj = colecao.find({"nome": "Administrador"})
    result = []


    for x in obj:
        result.append(x)

    
    return Auth.returnRequest(json.dumps(result, default=str))

@app.route('/users/<page_name>', methods=['GET'])
def usuario(page_name):
    # pageName = page_name
    obj = colecao.find({"nome": page_name})
    result = []
    for x in obj:
        result.append(x)
    return json.dumps(result, default=str)

# print(colecao.find_one())

@app.route('/auth/<token>', methods=['GET','POST'])
def authentication(token):

    try:

        # Pega o token passado no auth/token         
        param = Auth.decode_token(token,'leroz123')

        # Pega o valor do parametros nome e password se falhar vai pro except 
        user = param['nome']
        password = param['password']

        # Procura no banco de dados os determinados compos passados
        find = colecao.find({"nome": user, "password": password}).count()
        if(find > 0):

            # Define que o usuário está autorizado
            payload = {
                "Authrorization": True
            }
            
            # Gera o token do payload acima
            authorization = Auth.gen_token(payload,'leroz123')
            
            # Adiciona o token a um header 'Authorization' com baerer
            result = Auth.returnRequest()
            result.headers['Authorization'] = 'Bearer '+authorization
            return result
            # result = Auth.setHeader('Authorization','Baerer '+authorization)
        else:
            result = "Acesso Negado"
            return Auth.returnRequest(result)
    except:

        result = 'Não tem permissão para continuar'

        # result = Auth.getHeader()
        # result = json.dumps(Auth.decode_token(token,"leroz123"),default=str)
        # result = user +" "+password
        return Auth.returnRequest(result,status=200)


@app.route('/str2hash')    
def str2hash():
    return Auth.str2hash('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c')

@app.route('/ejwt')
def encondejwt():
    data = {
        "nome": "Administrador",
        "password": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
    }
    return Auth.gen_token(payload_data=data,key='leroz123')

@app.route('/djwt')    
def decodejwt():
    return Auth.decode_token()

# Mantém o servidor rodando
if __name__ == "__main__":
    app.run(debug=True)
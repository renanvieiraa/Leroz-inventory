
import os
from flask.wrappers import Request, Response
from pymongo import MongoClient
import json
import hashlib
import jwt


# connect = MongoClient()

# Faz os caminhos dos arquivos, e exporta para métodos
class _db:
    def __init__(self):
        self.pathFile = os.path.dirname(__file__)
        self.banco = json.load(open(pathFile+"/config.json","rt"))     
        # self.pathB   
        pass

    # Retorna corretamente o banco
    def host():
        return banco['db_path']
    
    # Retorna a porta definida no config.json
    def port():
        return banco['db_port']
    
    def banco():
        return banco['db_name']

pathFile = os.path.dirname(__file__)
banco = json.load(open(pathFile+"/config.json","rt"))   


# db = config['pathDB']+":"+config[]
connect = MongoClient(_db.host(),_db.port())
db = connect.lerozdb


class Auth:
    def __init__(self):
        
        return 
        
    
    def str2hash(string):
        return hashlib.sha256(str(string).encode('utf-8')).hexdigest()
    
    
    # Retorno da requisição, conteudo que irá retornar no corpo, o tipo de aplicação e code de retorno.
    def returnRequest(contentRequest='ok',type='application/json',status=200):
        r = Response(contentRequest,content_type=type,status=status)
        r.mimetype = type
        
        # r.headers.add("Authorization","Bearer "+token)
        return r


    # DEFINE UM NOVO HEADER, PARAMETROS KEY E VALUE
    def setHeader(key, value):
        r = Response().headers.add(key,value)
        return r

    # PEGA HEADER, PARAMETROS KEY
    def getToken(token):
        return str("teste")

    def login(username, passw):
        result_db = db.users.find({"nome":username, "password":passw})
        if(result_db.count() > 0):
            r = Auth.setHeader('teste',"teste")
        return print(r)
    
    # GENERATE TOKEN JWT STANDARD
    def gen_token(payload_data, key):
        # result = jwt.encode(obj_json,str(key),algorithm={"typ": "JWT"})
        result = jwt.encode(payload=payload_data,key=key)
        return result
    
    def decode_token(jwttoken,secret_key,hash_type="HS256"):
        result = jwt.decode(jwttoken,str(secret_key),algorithms=hash_type)
        return result



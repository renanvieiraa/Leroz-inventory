
import os
from flask.wrappers import Response
from pymongo import MongoClient
import json
import hashlib

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


print(db.users.find())

class Auth:
    def __init__(self, user_id, user_pass, token):
        
        pass
    
    def str2hash(string):
        return hashlib.sha256(str(string).encode('utf-8')).hexdigest()
    def setType(contentRequest='ok',type='application/json'):
        r = Response(contentRequest)
        r.mimetype = type
        return r

    def setHeader(key, value):
        # r = Response.headers.set(key, value)
        r = Response.headers[key] = value
        return r

    def login(username, passw):
        result_db = db.users.find({"nome":username, "password":passw})
        if(result_db.count() > 0):
            # r = Auth.setHeader('auth',hashlib.md5(str('Autorizado').encode('utf-8')).hexdigest())
            r = Auth.setHeader('teste',"teste")
        return print(r)



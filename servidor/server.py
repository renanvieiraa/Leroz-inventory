from collections import defaultdict
import flask
from flask import json
from flask.json import JSONDecoder, JSONEncoder, jsonify
from pymongo import MongoClient
from flask import Flask, Request, jsonify
cliente = MongoClient('mongodb://localhost:27017')

app = Flask(__name__)
db = cliente.dbmidias
colecao = db.posts

@app.route('/')
def index():
    return 'index page'

@app.route('/users',methods=['GET'])
def usuarios():
    
    obj = colecao.find({"nome": "renan José"})
    result = []

    for x in obj:
        result.append(x)
    return json.dumps(result, default=str)

@app.route('/users/<page_name>', methods=['GET'])
def usuario(page_name):
    pageName = page_name
    obj = colecao.find({"nome": page_name})
    result = []
    for x in obj:
        result.append(x)
    return json.dumps(result, default=str)

# print(colecao.find_one())


if __name__ == "__main__":
    app.run(debug=True)
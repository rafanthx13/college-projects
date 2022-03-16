from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from json import dumps

# Ler modulo proprio
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/src')
import textminig_code

# Lidar com Chamada Assincrona
app = Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin
def hello():
    return 'Hello, World!'

@app.route('/test2', methods = ['POST'])
@cross_origin()
def call_test():
	comentario = request.json['comentario']
	return jsonify(textminig_code.classifica(comentario))
	
if __name__ == '__main__':
	app.run(debug=True)

# flask
# flask_cors
# torch
# pandas

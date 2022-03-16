from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from json import dumps

# Ler modulo proprio
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/src')
import vc_cleaner_simple_api

# Lidar com Chamada Assincrona
app = Flask(__name__)
CORS(app)

@app.route('/simple_vc', methods = ['POST'])
@cross_origin()
def call_simple_vc():
	agent = {'position': request.json['startState'],
			'dirty' : {'A': request.json['dirtyA'], 'B': request.json['dirtyB'] }}
	return jsonify(vc_cleaner_simple_api.vc_cleaner_simple_api(agent)) # retorna como JSON
	
if __name__ == '__main__':
	app.run(debug=True)
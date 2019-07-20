import pandas as pd
from Neuron_re import Neuron_re

class Input_Layer:

	# Método Construtor da Camada Inicial
	def __init__(self, array_features):
		# Validando array de entrada de features
		if(bool(array_features) == False):
			raise SystemExit('array_features invalido')
		self.qtd_neurons = len(array_features) # Opctional
		self.array_features = array_features # list
		self.neurons_set = {} # dict {neuron_id ==> NeuronInstanceObject}
		# Cria n Neuronios da Camada Inicial, que são as N FEATURES passadas no array
		for neuron_id in array_features:
			neuron_input = Neuron_re(neuron_id)
			self.neurons_set[neuron_id] = neuron_input

	# Exemplo: input_dict_xl => {1: {'Pclass': 3, 'Sex': 1, 'Age': 22, 'SibSp': 1, 'Parch': 0}}
	# OBJ: Inserir em cada neuronio uma dictionario contendo os dados de seu respectivo campo {passenger id =>your_data}
	def inserting_inputs_in_neurons(self, input_dict_features):
		for passenger_id, dict_data in input_dict_features.items():
			for neuron_id, data in dict_data.items():
				self.neurons_set[neuron_id].list_data[passenger_id] = data

	# OBJ: ler CSV e retornar:
	# xk = {Passenger_ID => (tuple)} | djk = {PassgerID => Survived}
	def reading_csv(self, file_path):
		# Colocar a media de idade por classe e tornala em inteiro
		# Usada no aaply da coluna de 'Age' para corrigila
		def handler_age(row_age_pclass):
			age = row_age_pclass[0]
			# Se nao tiver Pclass
			if( not ('Pclass' in row_age_pclass)):
				if(pd.isnull(age)):
					return 31
				else:
					if(age < 0):
						return int(np.ceil(age))
					else:
						return int(age)
			# Quando tiver Pclass
			pclass = row_age_pclass[1]
			if(pd.isnull(age)):
				if(pclass == 1):
					return 37
				elif(pclass == 2):
					return 29
				else:
					return 24
			else:
				if(age < 0):
					return int(np.ceil(age))
				else:
					return int(age)
		# Leitura de CSV
		df = pd.read_csv(file_path, encoding = 'utf-8', sep=',', header = 0)
		# Array de Colunas padrao
		array_default = ['PassengerId', 'Survived']
		array_default.extend(self.array_features)
		# Tratamento de CSV
		df = df[ array_default ] # Pegando somente as Colunas
		# Tratar cada Coluna
		if('Age' in self.array_features and not 'Pclass' in self.array_features):
			df['Age'] = df[ ['Age'] ].apply(handler_age, axis = 1) # Trata a idade
		if('Age' in self.array_features and 'Pclass' in self.array_features):
			df['Age'] = df[ ['Age','Pclass'] ].apply(handler_age, axis = 1) # Trata a idade
		if('Sex' in self.array_features):
			df['Sex'] = pd.get_dummies(df['Sex'], drop_first = True) # Tratar Variavel categorica de Sex ==> 0  e 1 [1 ==> male/ 0 ==> female]
		# Inicializar xk e djk
		xk = {}  # {Passenger_ID => (tuple_features)}
		djk = {} # {Passenger_ID => Survived}
		for index, row in df.iterrows():
			xk[row['PassengerId']] = (row[self.array_features].to_dict()) # sera das colunas escolhidas
			djk[row['PassengerId']] = row['Survived']
		return xk, djk
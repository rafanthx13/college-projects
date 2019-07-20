class Neuron_re:

	# Constuctor
	def __init__(self, neuron_id):
		self.neuron_id = neuron_id # 'Age'/''Sex'/'Fare'/'Output'
		self.list_data = {} # {passanger id => data (of type neuron_id)}
		self.weights = {} # {feature ==> weight}

	# Soma : Somatorio dos produtos entre um dado e o peso do neuronio
	# dict_data : Example : {'Pclass': 3, 'Sex': 0, 'Age': 26, 'SibSp': 0, 'Parch': 0}
	def soma(self, dict_data):
		s = 0
		for feature, value in dict_data.items():
			s += self.weights[feature] * value
		return s

	# Função Degrau
	def step_function(self,x):
		return 1 if x >= 0 else 0

	# __str__ : A representaçâo do Obejto ao dar um print nele
	def __str__(self):
		newline,  newlineline, spaces = '\n\t', '\n\t\t', '     '
		str_output = ['\n' + 'Neuron: ' + self.neuron_id]
		neuron_weights = '' 
		if(bool(self.weights)):
			neuron_weights = newline + '.weights ==> ' + newlineline
			for feature in self.weights.keys():
				if(feature == 'PassengerId'):
					neuron_weights += feature + '\t|' + str(self.weights[feature]) + newlineline
				else:
					neuron_weights += feature + spaces + '\t|' + str(self.weights[feature]) + newlineline
		else:
			neuron_weights += ' None'
		str_output.append(neuron_weights[:-3])
		return ''.join(str_output)
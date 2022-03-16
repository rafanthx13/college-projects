
class Neuron:

	# Constuctor
	def __init__(self, neuron_id):
		self.neuron_id = neuron_id # 'Age'/''Sex'/'Fare'
		self.list_data = {} # {passanger id => data (of type neuron_id)}
		self.neuron_link_weights_next = {} # {obj_anteiror ==> weight}
		self.neuron_link_weights_back = {} # {obj_proximo ==> weight}

	# Soma : Somatorio dos produtos entre um dado e o peso do neuronio
	def soma(self, passenger_id):
		s = 0
		for neuron, weight in self.neuron_link_weights_back.items():
			s += neuron.list_data[passenger_id] * weight
		return s

	# Função Sigmoide, não é util
	def sigmoid_function(self, x):
		 return 1 / (1 + math.exp(-x))

	# Função Degrau
	def step_function(self,x):
		return 1 if x >= 0 else 0

	# Aplicação da Sigmoide sobre a Soma pelo para cada conjunto de dado de passenger_id
	def neuron_output(self, passenger_id):
		return self.step_function(self.soma(passenger_id))
		
	# Link de um neuronio com um conjutno que ficara atras dele
	def link_neurons_back(self, list_neurons):
		for neuron in list_neurons:
			self.neuron_link_weights_back[neuron] = None # so inicializa  os pesos
			neuron.neuron_link_weights_next[self] = None # so inicializa

	# Insere peso entre voce e um neuronio da Frente
	def set_weights_next(self, neuron_next, weight):
		self.neuron_link_weights_next[neuron_next] = weight
		# neuron_next.neuron_link_weights_back[self] = weight # Sera util em Multicamada DEIXAR COMENTADO

	# Insere peso entre voce e um neuronio de traz
	def set_weight_back(self, neuron_back, weight):
		self.neuron_link_weights_back[neuron_back] = weight
		# neuron_back.neuron_link_weights_next[self] = weight # Sera util em Multicamada DEIXAR COMENTADO

	# __str__ : A representaçâo do Obejto ao dar um print nele
	def __str__(self):
		newline = '\n\t'
		newlineline = '\n\t\t'
		spaces = '     ' # 5
		
		str_output = [ '\n' + 'Neuron: ' + self.neuron_id]

		if(bool(self.neuron_link_weights_back)):
			neuron_title_back = newline + '.neuron_link_weights_back ==>' + newlineline
			neurons_back = ''
			for neuron_back, w in self.neuron_link_weights_back.items():
				if(neuron_back.neuron_id == 'PassengerId'):
					neurons_back += neuron_back.neuron_id + '\t| ' + str(w) + newlineline
				else:
					neurons_back += neuron_back.neuron_id + spaces + '\t| ' + str(w) + newlineline
				neuron_title_back += neurons_back
				neurons_back = ''
		else:
			neuron_title_back = newline + '.neuron_link_weights_next ==> None'
		
		if(bool(self.neuron_link_weights_next)):
			neuron_title_next = newline + '.neuron_link_weights_next ==>' + newlineline
			neurons_next = ''
			for neuron_next, w in self.neuron_link_weights_next.items():
				if(neuron_next.neuron_id == 'PassengerId'):
					neurons_next += neuron_next.neuron_id + '\t| ' + str(w) + newlineline
				else:
					neurons_next += neuron_next.neuron_id + spaces + '\t| ' + str(w) + newlineline
				neuron_title_next += neurons_next
				neurons_next = ''
		else:
			neuron_title_next = newline + '.neuron_link_weights_next ==> None' + '\n'

		str_output.append(neuron_title_back[:-3])
		str_output.append(neuron_title_next)
		
		return ''.join(str_output)
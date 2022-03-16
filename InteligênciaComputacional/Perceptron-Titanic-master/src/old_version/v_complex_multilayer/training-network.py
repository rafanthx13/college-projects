import os
import sys
from random import uniform
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/class')
from Input_Layer import Input_Layer
from Neuron import Neuron

##########################################################
	# Titulo
print('\tRede Neural - Perceptron Simples para Problema do Titanic\n')

# Constante Iniciais
file_path = ('../../dataset/train.csv') # file_path do csv
array_features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch'] # array de Features usadas

input_layer = Input_Layer(array_features)
xk, djk = input_layer.reading_csv(file_path)
# xk  = dict{PassengerId => dict{Pclass => data}}
# djk = dict{PassengerID => Survived(0/1)}

# Verificando Pesos Iniciais dos neuronios de entrada
output_neuron = Neuron('Output')

# Linkando Neuronio de saida com os neuronios de Entrada
output_neuron.link_neurons_back(input_layer.neurons_set.values())

# Inserindo list_data nos neuornuos ==> carregando dadso em cada neuronio (OK!)
input_layer.inserting_inputs_in_neurons(xk)

# Setando Pesos Iniciais como aleatorios entre [0,1]
for neuron_input_layer in input_layer.neurons_set.values():
	output_neuron.set_weight_back(neuron_input_layer, uniform(0,1))

###############################################################################
	# Treinamento da Rede

print('Iniciando Treinamento')
# Setando constantes Iniciais
learning_rate = 0.1 
limit_epoch = 10
foi_igual = 0
epoch = 1
while (epoch != limit_epoch):
	for passenger_id in djk.keys():
		neuron_output = output_neuron.neuron_output(passenger_id)
		if(neuron_output != djk[passenger_id]):
			for neuron, weight in output_neuron.neuron_link_weights_back.items():
				output_neuron.neuron_link_weights_back[neuron] += (learning_rate * (djk[passenger_id] - neuron_output) * neuron.list_data[passenger_id])
	epoch += 1
print('Fim do Treinamento')

###############################################################################
	# Execução da Rede sobre os mesmos dados

acertos, erros = 0, 0
for passenger_id in djk.keys():
	neuron_output = output_neuron.neuron_output(passenger_id)
	if(neuron_output == djk[passenger_id]):
		acertos += 1
	else:
		erros += 1
print('\nExecucao da rede treinada em', epoch, 'epocas')
print('Acertos :', acertos,'/', 891)
print('Erros :', erros, '/', 891 )
print('Porcentagem de Acerto :', "{:.2%}".format(acertos/891)) # tranforma em porcentagem

print(output_neuron) # Mostrando pesos no final
print('Happy End')
import os, sys
from random import uniform
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/class')
from Input_Layer import Input_Layer
from Neuron_re import Neuron_re

##########################################################
	# Titulo
print('\tRede Neural - Perceptron Simples para Problema do Titanic\n')

# Constante Iniciais
file_path = ('../../dataset/train.csv') # file_path do csv
array_features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch'] # array de Features usadas
array_features = ['Sex']

input_layer = Input_Layer(array_features)
xk, djk = input_layer.reading_csv(file_path)
# xk  = dict{PassengerId => dict{Pclass => data}}
# djk = dict{PassengerID => Survived(0/1)}

# Verificando Pesos Iniciais dos neuronios de entrada
output_neuron = Neuron_re('Output')

# colocando valores aleartorios iniciais dos pesos
for feature in array_features:
	output_neuron.weights[feature] = uniform(0,1)

print(output_neuron)

###############################################################################
	# Treinamento da Rede

print('\nIniciando Treinamento')
# Setando constantes Iniciais
learning_rate = 0.1 
limit_epoch = 10
foi_igual, epoch = 0, 1
while (epoch != limit_epoch):
	for passenger_id in djk.keys():
		soma = output_neuron.soma(xk[passenger_id])
		result = output_neuron.step_function(soma)
		if(result != djk[passenger_id]):
			for feature in array_features:
				output_neuron.weights[feature] += learning_rate * (djk[passenger_id] - result) * xk[passenger_id][feature]
	epoch += 1
print('Fim do Treinamento')

###############################################################################
	# Execução da Rede sobre os mesmos dados

acertos, erros = 0, 0
for passenger_id in djk.keys():
	soma = output_neuron.soma(xk[passenger_id])
	result = output_neuron.step_function(soma)
	if(result == djk[passenger_id]):
		acertos += 1
	else:
		erros += 1
print('\nExecucao da rede treinada em', epoch, 'epocas')
print('Acertos :', acertos,'/', 891)
print('Erros :', erros, '/', 891 )
print('Porcentagem de Acerto :', "{:.2%}".format(acertos/891)) # tranforma em porcentagem

print(output_neuron) # Mostrando pesos no final
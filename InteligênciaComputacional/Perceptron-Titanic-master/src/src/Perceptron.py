import math

class Perceptron:
        # Constuctor
        def __init__(self, weights):
                self.weights = weights # {feature ==> weight}

        def soma(self, dict_data):
                s = 0
                for feature, value in dict_data.items():
                        s += self.weights[feature] * value
                return s

        def sigmoide(self, soma):
                return 1 / (1 + math.exp(-soma))


	# Função Degrau
        def step_function(self,x):
                return 1 if x >= 0 else 0

        def neuron(self, features):
                u = self.soma(features)
                y = self.step_function(u)
                return y
	
        def __str__(self):
                newline,  newlineline, spaces = '\n\t', '\n\t\t', '     '
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


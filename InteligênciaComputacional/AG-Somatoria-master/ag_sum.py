# Programa em Python para somatoria
# Grupo: Bruno B, Rafael M. A. (Julho de 2018 Ufu-2018-01)

from random import randint, random
import matplotlib.pyplot as plt
from math import ceil
import pandas as pd
import time, os

class Individuo():
	
	# Static variable
	length = None
	target = None
	mutant_rate = None
	
	# Construtor
	def __init__(self, generation = 0):
		self.generation = generation
		if(generation >= 0):
			self.cromossomo = self.insert_individuals()
			self.fitness = self.calculate_fitness() # quanto menor melhor
		else:
			# para inicializar sem presisar fazer o insert_individuals e fitnes, 
			# pois o cromossomo vira de crossover
			self.cromossomo = []
			self.fitness = 99999

	def insert_individuals(self):
		individuals = []
		count = 0
		while(count < self.length):
			temp = (randint(0, self.target))
			if(temp not in individuals):
				individuals.append(temp)
				count += 1
		return individuals
		# return [ randint(0,target) for x in range(0,length) ]

	def calculate_fitness(self):
		sum = 0
		for value in self.cromossomo:
			sum = sum + value
		return abs(self.target - sum)

	# retorna algo diferente de 1 se tem elemetno duplicado
	def index_duplicate(self, cromossomo):
		count = 0
		for item in cromossomo:
			qtd = cromossomo.count(item)
			if(qtd > 1):
				return cromossomo.index(item)
		return -1

	# juncao de crossover mais mutacao: Foi usado o PMX , porem, quando tinha duplicado, s
	# sorteia do outro algum index e verfica se ainda tem duplicada
	def crosoover(self, another_individual):
		son_1 = Individuo(-1)
		son_2 = Individuo(-1)

		# definindo pontos de corte
		start_point = randint(0, self.length - 1) # -2, pois ai nao
		end_point = randint(0, self.length - 1)

		# Os pais devem ser diferente para que nao haja deadlock
		if(start_point != end_point and self.cromossomo != another_individual.cromossomo):
			
			# star nao pode ser maior que end, entao troca (sabemos que eles nao serao iguais)
			if(start_point > end_point):
				aux = start_point
				start_point = end_point
				end_point = aux

			# Faz a troca das listas
			son1 = self.cromossomo[:start_point] + another_individual.cromossomo[start_point:end_point] + self.cromossomo[end_point:]
			son2 = another_individual.cromossomo[:start_point] + self.cromossomo[start_point:end_point] + another_individual.cromossomo[end_point:]

			# Verificia se tem duplicado, se houver, troca
			# filho1
			while True:
				indx_duplicate = self.index_duplicate(son1)
				# verifica se tem duplicado
				if(indx_duplicate != -1):
					# tem duplicado
					son1[indx_duplicate] = son2[randint(0, self.length - 1)]
				else:
					# sai, nao tem duplicado
					break
			# filho 2
			while True:
				indx_duplicate = self.index_duplicate(son2)
				if(indx_duplicate != -1):
					son2[indx_duplicate] = son1[randint(0, self.length - 1)]
				else:
					break
		else:
			# entao eles irao paa proxima geração 
			son1 = self.cromossomo
			son2 = another_individual.cromossomo

		# Complemenando inividuo atualizando seus dados
		son_1.cromossomo = son1
		son_2.cromossomo = son2

		son_1.mutation()
		son_2.mutation()

		son_1.generation = self.generation + 1
		son_2.generation = another_individual.generation + 1
		
		son_1.fitness = son_1.calculate_fitness()
		son_2.fitness = son_2.calculate_fitness()

		return son_1, son_2

	# mutacao inplace
	def mutation(self):
		for key, element in enumerate(self.cromossomo):
			if(random() < self.mutant_rate):
				while True:
					# mutaço
					self.cromossomo[key] = randint(0, self.target - 1)
					# busca se ficou duplicado
					if(self.index_duplicate(self.cromossomo) == -1):
						break
	
	# Prepresentation of class when to print
	def __str__(self):
		text1 = 'Geracao: ' + str(self.generation) + '| Fitness: ' + str(self.fitness) + '\n Cromossomo: '
		text2 = ', '.join(str(x) for x in self.cromossomo)
		return text1 + '[' + text2 + ']'

############################################

class AlgoritmoGenetico():

	length_solution = 0

	def __init__(self, size_population, length_solution):
		self.length_solution = length_solution
		self.size_population = size_population
		self.population = []
		self.generation = 0
		self.best_fit = None

	def initialize_population(self):
		for i in range(0, self.size_population):
			self.population.append(Individuo(self.generation))

	# Ordena para encontrr o melhor inidividuo, o melhor por geracao fica em _outside_list
	def sort_population(self):
		self.population = sorted(self.population, key = lambda ind: ind.fitness)
		the_best = self.population[0]
		# Vamos criar uma copia do Objeto para garantir que seja um  novo valor na memoria (Sem isso Buga)
		best_of_generation = Individuo(-1)
		best_of_generation.cromossomo = the_best.cromossomo.copy()
		best_of_generation.fitness = the_best.calculate_fitness()
		best_of_generation.generation = the_best.generation
		# Copiando
		_outside_list.append(best_of_generation)
		# mudar para quando best_fit == none, o inicial
		if(self.generation == 0): # na 1 vez nao ha com q comparar
			# inicialmente tem que comecar com algum valor
			self.best_fit = best_of_generation
		elif(self.best_fit.fitness > best_of_generation.fitness):
			 # o atual dessa geraçao é melhor que a outra solucao, entao troca
			self.best_fit = best_of_generation

	# Por torneio siples: Escolhe populacao/5 individuos de forma aleartoria e selecionar o melhor deles
	def selection_tournament(self):
		choseds = []
		for i in range(0, ceil(size_population/5)):
			index = randint(0, size_population - 1)           
			choseds.append( (self.population[index], index))
		choseds = sorted(choseds, key = lambda ind: ind[0].fitness)
		return choseds[0][1] # retorna somente o index no original

	def __str__(self):
		return str(self.best_fit)

############################################

global _outside_list
_outside_list = []

# Deixe habilitada para o usuario inserir os dados
target = int(input('Digite o numero a ser buscado:\n==> '))
start_length = int(input('Digite o Numero de n Valores:\n==> '))

# Input Hardcode : Desabilita quando o usuario for inserir
#target = 800000
#start_length = 300
mutant_rate = 0.10 # entre [0,1]

# Insere variaveis staticas
Individuo.length = start_length
Individuo.target = target
Individuo.mutant_rate = mutant_rate

# Tamnaho da populaçao HardCode
size_population = 100
ages = 500 # quantidades de gerações

# Titulo e Tempo
print('Ag - Somatoria - Buscando', str(start_length), 'numeros para', str(target), flush = True)
targetime = time.time()

# Iniciar população
enviroment = AlgoritmoGenetico(size_population, start_length)
enviroment.initialize_population()
enviroment.sort_population()

# Começa de 0 até age
while(enviroment.best_fit.fitness != 0 and enviroment.generation < ages):
	# Nao encontrou ainda, entao, vai fazer até  achar o melhor ou atingir o max
	new_population = []
	# Geranco nova populaçâo
	for times in range(ceil(enviroment.size_population/2)):
		# print(times, flush = True)
		father1_index = enviroment.selection_tournament()
		father2_index = enviroment.selection_tournament()
		# garantir diversidade
		while(father2_index == father1_index):
			father2_index = enviroment.selection_tournament()
		# Selecao
		father1 = enviroment.population[father1_index]
		father2 = enviroment.population[father2_index]
		# Crosoover + mutacaço interna
		son1, son2 = father1.crosoover(father2)
		new_population.append(son1)
		new_population.append(son2)
	# Reinserção : gerou uma nova populaçâo
	enviroment.population = new_population
	enviroment.generation += 1
	enviroment.sort_population()

# Tempo final
end_time = time.time()
time_training = round(end_time - targetime, 3)

# Quando sair por que acho o melhor
if(enviroment.best_fit.fitness == 0 and enviroment.generation < ages):
	print('\n\tEncontrado uma Resposta Ideal:')
	print(enviroment.best_fit)
# saiu por que atinigiu o max 
else:
	print('\n\tChegou ao Limite de epocas:', enviroment.generation)
	print('\n\tA Melhor Resposta das Geracoes:')
	print(enviroment.best_fit) # O melhor das geraçôes, nao presisa ordenar

print('\nSum:', str(sum(enviroment.best_fit.cromossomo)))
print('Tempo de Treinamento :', time_training, 'segundos', flush = True)

#### Salvando em CSV dados de estatistias gerais
labels = ['Target', 'Epochs_Total', 'Time', 'Find_in_Generation', 'Delta_Value_Found']
file_path = 'general_statistics.csv'
row = [(tuple([target, ages, str(time_training).replace('.',','), enviroment.best_fit.generation, enviroment.best_fit.fitness] ))]
df = pd.DataFrame(row, columns = labels)
if(not os.path.isfile(file_path)):
	df.to_csv(file_path, sep = ';', index = False)
else:
	df.to_csv(file_path, sep = ';', index = False, mode = 'a', header = False)

#### Salvar e Plotar Grafico de Convergencia
try:
	ages_process = range(0,enviroment.generation + 1)
	list_fitness = [x.fitness for x in _outside_list] # compressao de lista
	fig, axes = plt.subplots(figsize=(8,5))
	axes = plt.plot(ages_process, list_fitness)
	plt.grid()
	plt.xlabel('Épocas')
	plt.ylabel('fitness')
	plt.title('Gráfico de Convergência do AG.' + ' n = ' + str(start_length) + '| t = ' + str(target) )
	fig.savefig("ag-convergence.png")
except Exception as e:
	print('Erro ao salvar grafico')
	print('_outside_list', len(_outside_list))
	print('enviroment.best_fit.generation + 1', enviroment.generation + 1)
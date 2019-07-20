# Programa em Python para somatoria
# Grupo: Bruno B, Eduardo F., Rafael M. A. (Julho de 2018 Ufu-2018-01)

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

global _outside_list
_outside_list = []
size_population = 100
ages = 500# quantidades de gerações


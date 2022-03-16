class Node:
	""" 
	Representa um nó da árvore de Busca
		Estado: Tripla (Posição(str:'A','B'), Sujo(bool), Sujo(bool))
		Ação: Ação que veio do pai para chegar nesse nó
		Origem: é no nó Pai, para intercalar os nós e formar a árvore
		Custo: Custo da ação, poderá ser fixo ou variável dependendo da Busca
		Level: Profundidade do Nó
		True ==> Sujo, False  ==> Limpo
	"""

	# Constantes Estáticas: Compartilhadas pelos objetos
	VACCUM, LEFT, RIGHT = "clean", "left", "right"
	POSITION, DIRTY_A, DIRTY_B = 0, 1, 2
	MAP_POSITION_DIRTY = {"A": DIRTY_A, "B": DIRTY_B}

	# Constructor
	def __init__(self, state, action, origin, cost, level):
		self.state  = state   	# Tuple: Tripla (str('A'/'B'),bool,bool) 
		self.action = action    # str | 1° 'Start' | L° 'End'
		self.origin = origin    # Node Object Pointer | 1° None
		self.cost   = cost      # int | 1° 0
		self.level  = level     # int | 1° 0

	# Testa se chegou no objetivo ou não
	def target_test(self):
		return self.state[Node.DIRTY_A] == False and self.state[Node.DIRTY_B] == False

	# Dado a action, de acordo com o nó atual, gera um novo nó
	def action_node(self, action):
		new_cost  = self.cost  + 1 # custo unitario
		new_level = self.level + 1
		# Ação: VACCUM
		if(action == Node.VACCUM):
			if(self.state[Node.MAP_POSITION_DIRTY[self.state[Node.POSITION]]] == False):
				# Esta limpo e limpa = sem mudança
				return Node((self.state), self.VACCUM, self, new_cost, new_level)
			else:
				# Esta sujo e Limpa = limpa dependeno de onde está
				if(self.state[Node.POSITION] == 'A'):
					vaccum_action = (self.state[Node.POSITION], False, self.state[Node.DIRTY_B])
				else:
					vaccum_action = (self.state[Node.POSITION], self.state[Node.DIRTY_A], False)
				return Node(vaccum_action, Node.VACCUM, self, new_cost, new_level)
		# Ação: LEFT
		elif(action == self.LEFT):
			if(self.state[Node.POSITION] == 'A'):
				# Está a esquerda e vai para esquerda = sem mudança
				return Node(self.state, self.LEFT, self, new_cost, new_level)
			else:
				# direita => LEFT => esquerda === Executa movimento para esquerda de B para A
				return Node( ('A', self.state[self.DIRTY_A], self.state[self.DIRTY_B]),
					Node.LEFT, self, new_cost, new_level)
		# Ação: RIGHT
		elif(action == Node.RIGHT):
			if(self.state[Node.POSITION] == 'B'):
				# Está a direita e vai para direita = sem mudança
				return Node(self.state, self.RIGHT, self, new_cost, new_level)	
			else:
				# esquerda => RIGHT => direita === Executa movimento para direita de A para B
				return Node( ('B', self.state[Node.DIRTY_A], self.state[Node.DIRTY_B]),
					 Node.RIGHT, self, new_cost, new_level)
		# Ação: ERROR: String invalida
		else:
			print("\nERROR: A acao digitada: '" + action + "' nao eh valida")
			print("As strings de entrada devem ser somente: ")
			print("\t" + self.VACCUM, self.RIGHT, self.LEFT)
			exit(101)

	# String a ser imprimida ao dar um print num objeto
	def __str__(self):
		str_output = "[ S: ("
		for attr in self.state:
			str_output += str(attr) + ','
		str_output = str_output[:-1] + ')'
		str_output += ', A: ' + str(self.action)
		str_output += ", C: " + str(self.cost) + ", L: " + str(self.level) + " ]"
		return str_output

	# Comparar um nó com outros pelo operador '=='
	def __eq__(self, other_node): 
		if(other_node is None):
			return False
		return self.state == other_node.state

	# Encapsula e inicializa a lista de retorno de sequencias de ações feito no final
	def sequence_of_action(self):
		return self.recursive_return([], self.level, self.cost)

	# retorno recursivo para retornar lista de açoes/estados, level e custo
	# Eh necessário executar reverse() após a saida para está na ordem
	def recursive_return(self, array_state_actions, level, cost):
		array_state_actions.append({
				'position': self.state[Node.POSITION], 
				'dirty': {
					"A": self.state[Node.DIRTY_A],
					"B": self.state[Node.DIRTY_B]},
				'action': self.action}
		)
		return_data = {'state_sequence': array_state_actions, 'level': level, 'cost': cost}
		if(self.origin is None):
			return return_data
		self.origin.recursive_return(array_state_actions, level, cost)
		return return_data
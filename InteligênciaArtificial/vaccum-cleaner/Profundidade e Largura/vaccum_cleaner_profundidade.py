from resource import functions as f
from resource.Node import Node

#### True ==> Sujo, False  ==> Limpo
#### Inicialização de Variáveis

# Lista de açoes
list_actions = ['left','clean','right']
count_node = 0
border = []
last_node = None
final_node = None

# Escolhendo o estado inicial
start_state = f.chose_start_state()		
# Criação do primeiro nó, deve ser dessa forma, pai == None, com o estado inicial e tudo zerado
start_node = Node( f.convert_tripla(start_state), 'Start', None, 0, 0)

#####################################################

### Busca em profundidade Limitada ao tamanho 8 ###
def busca_profundidade(node, limite):
	global count_node
	cut_ocorrence = False
	if(node.target_test()):
		return node
	elif(node.level == limite):
		return 'cutoff' # quando encontrar o corte
	else:
		for action in list_actions: 
			son = node.action_node(action)
			count_node += 1
			result = busca_profundidade(son, limite)
			# cai quando chegar no corte
			if(isinstance(result, str)):
				cut_ocorrence = True
			# Retorna
			elif(result != None):
				return result
	if(cut_ocorrence == True):
		return 'cut'
	else:
		return None

# Executando
print('\nstart-node:',start_node, '\n')
final_node = busca_profundidade(start_node, limite = 8)
print(f.only_actions(final_node.sequence_of_action()))
print('\nSequencia de Acoes para\n\t', final_node)
f.print_formatted_sequence(final_node.sequence_of_action())
print('count nodes:', count_node)

#####################################################

### BUSCA EM PROFUNDIDADE SEM LIMITES : ATÉ EXCEPTIOON DA MEMORIA ###

# # Função recursiva de profundidade
# def busca_profundidade(node):
# 	global last_node  # global serve para acessar o endereço das varaiveis fora desse escopo
# 	global count_node
# 	last_node = node
# 	if(node.target_test()):
# 		return node
# 	for action in list_actions: 
# 		son = node.action_node(action)
# 		count_node += 1
# 		border.append(son)
# 		next_node = border.pop() # retira como uma pilha, do ultimo (right)
# 		busca_profundidade(next_node) # recursao

# # Execução
# border.append(start_node)
# try:
# 	obj_node = busca_profundidade(border.pop())
# 	print('Chegou ao no objetivo')
# 	print(last_node)
# 	print(obj_node)
# 	final_node = obj_node
# except RecursionError:
# 	print('RecursionError')
# 	print('Ultimo No da execucao:', last_node)
# 	final_node = last_node	
# print('Quantidade de nos gerados:', count_node)


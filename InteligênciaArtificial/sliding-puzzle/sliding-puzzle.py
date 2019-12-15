# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2

from resources import functions as f
from resources.Game import Game
import queue as Q

## Insere estado inicial manualmente
start_state = f.get_start_state()	

## HardCode que funciona
#start_state = ('5', '8', '3', '6', '4', '_', '7', '2', '1') 	# Funciona
#start_state = ('7', '2', '4', '5', '_', '6', '8', '3', '1')	# Funciona

#print game
print('\n\tEstado inicial\n')
f.print_game(start_state)

h_options = [1,2]
count_nodes = {1: 0, 2: 0}
count_states = {1: 0, 2: 0}
count_nodes_expandeds = {1: 0, 2: 0}
final_level = {1: 0, 2: 0}
count_put_queue = {1: 0, 2: 0}

for option in h_options:

	# Inicialização do Processo
	Game.h_option = option 		 		# Insere Heuristica
	priority_border = Q.PriorityQueue()	# Fila de prioridade por f(n)
	explorateds_states = {}				# Dicionario de estados explorados: Funciona como Hash
	node = Game(start_state, f.get_empty_space(start_state), None, 'Start', 0, 0)
	priority_border.put(node)
	print('\n\n\t\tGame com a heuristica: h' + str(option), '\n\n')

	# Algoritmo A*: Busca de nó na fila de prioridade baseado em f(n) = h(n) + g(n)
	while True:
		# Flha: Borda Vazia
		if(priority_border.empty()):
			print('\n\tBorda Vazia: Nao encontrou sequencia\n')
			break
		node = priority_border.get()
		# Encontrou estado objetivo
		if(node.test_goal()):
			print('\n\tEncontrou Estado Objetivo\n')
			node.print_game_recursive()
			f.print_array_actions(node.sequence_of_actions())
			final_level[option] = node.level
			#print(f.print_formatted_sequence(node.sequence_of_actions()))
			break
		# Executando as ações possíveis
		for action in node.list_actions():
			count_nodes[option] += 1
			son = node.execute_action(action)
			try:
				# Verifica se existe esse estado no explorateds_states: Se exsitir não insere
				bool(explorateds_states[son.generate_hash()])
			except:
				# Se não existir esse estado, então insere na fila
				priority_border.put(son)
				count_put_queue[option] += 1
		explorateds_states[node.generate_hash()] = True # Pôe em explorateds_states
		count_nodes_expandeds[option] += 1
	# Nos Expandidos
	count_states[option] = len(explorateds_states)

print('\n\t\tResultado Final')
for option in h_options:
	print('\th' + str(option))
	print('Porfundidade para h' + str(option), '==>', final_level[option])
	print('Nos Gerados para h' + str(option), '==>', count_nodes[option])
	print('Nos Expandidos para h' + str(option), '==>', count_states[option]) 
	print('Nos colocados na Fila para h' + str(option), '==>', count_put_queue[option])
	print('Nos gerados e nao entraram fila para h' + str(option), '==>', (count_nodes[option] - count_put_queue[option]))

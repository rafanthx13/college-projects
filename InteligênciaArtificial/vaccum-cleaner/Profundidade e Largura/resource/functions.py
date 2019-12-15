# True ==> Sujo, False  ==> Limpo

# cmd gui: Retorna Tripla (Posicao(str), DirtyA(bool), DirtyB(bool)) 
def chose_start_state():
	agent = {'position' : '', 'dirty': {"A": None, "B": None}}
	while(agent['position'] != 'A' and agent['position'] != 'B'):
		agent['position'] = input('Digite em qual lugar vai esta, A ou B\n==> ').upper()
	for p in agent['dirty'].keys():
		while(agent['dirty'][p] is None):
			aux = input(p + ') Digite T: Posicao ' + p + ' suja | F: Posicao ' + p + ' limpa\n==> ')
			if(aux in ['T','t']):
				agent['dirty'][p] = 'True'
			elif(aux in ['F','f']):
				agent['dirty'][p] = 'False'
	return (agent['position'], agent['dirty']['A'], agent['dirty']['B'])

# Print da sequence final de forma organizada
def print_formatted_sequence(array_sequence):
	array_sequence['state_sequence'].reverse()
	for state in array_sequence['state_sequence']:
		print(state['action'])
		a = 'Clean' if state['dirty']['A'] == False else 'Dirty'
		b = 'Clean' if state['dirty']['B'] == False else 'Dirty'
		print("(" + state['position'] + ',' + a + ',' + b + ')')
	print('END', 'level: ' + str(array_sequence['level']), 'cost: ' + str(array_sequence['cost']))

# Converte tripla de saida de chose_start_state
def convert_tripla(tripla):
	return (tripla[0], bool(tripla[1] == 'True'), bool(tripla[2] == 'True'))

def only_actions(array_sequence):
	array_sequence['state_sequence'].reverse()
	list_only_actions = []
	for state in array_sequence['state_sequence']:
		list_only_actions.append(state['action'])
	return list_only_actions
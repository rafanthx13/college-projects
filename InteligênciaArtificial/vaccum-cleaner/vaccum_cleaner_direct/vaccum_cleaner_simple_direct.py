# Roda o VaccumClenaer direto nesse aruivo, ou seja, nao usa o server

from copy import deepcopy # o copy normal nao vai copiar o  dict'dirty', vai copiar a referencia, por isso dava erro

# Inserçâo de Dados
opposite = {'A':'B', 'B':'A'}
agent = {'position' : '', 'dirty': {"A": None, "B": None}}
state_sequence = []

# Inseridno Posicao
while(agent['position'] != 'A' and agent['position'] != 'B'):
	agent['position'] = input('Digite em qual lugar vai esta, A ou B\n==> ').upper()

# Inserrindo Sujeira
for p in agent['dirty'].keys():
	while(agent['dirty'][p] is None):
		aux = input(p + ') Digite T: Posicao ' + p + ' suja | F: Posicao ' + p + ' limpa\n==> ')
		if(aux in ['T','t']):
			agent['dirty'][p] = 'True'
		elif(aux in ['F','f']):
			agent['dirty'][p] = 'False'

state_sequence.append({'agent': deepcopy(agent), 'action':'start'})
while('True' in agent['dirty'].values() ):
	p_now = agent['position']
	if(agent['dirty'][p_now] == 'True'): # Limpa
		agent['dirty'][p_now] = 'False'
		state_sequence.append({'agent' : deepcopy(agent), 'action' : 'clean'})
	else: # Move para o lado oposto
		other_side = opposite[p_now]
		agent['position'] = other_side
		state_sequence.append({'agent' : deepcopy(agent), 'action' : 'move to ' + other_side})

print('\nSequencia de Estados e Acoes:')
for state in state_sequence:
	print_dirty = state['agent']['dirty'][state['agent']['position']] # para reduzir a linha
	space = '\t==> ' if print_dirty == 'True' else '\t==> ' # acrescenta espaço a mais pra ficar alinhado
	print('    ' + state['action'] + space + '(' + state['agent']['position'] + ',' + print_dirty + ')')
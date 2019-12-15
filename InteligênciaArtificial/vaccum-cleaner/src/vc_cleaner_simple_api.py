from copy import deepcopy # o copy normal nao vai copiar o  dict'dirty', vai copiar a referencia, por isso dava erro

def vc_cleaner_simple_api(agent):
	opposite = {'A':'B', 'B':'A'} # Auxiliar
	state_sequence = [] # Array que guarda a sequencia de Ações
	state_sequence.append({'agent': deepcopy(agent), 'action':'start'}) 
	while(True in agent['dirty'].values() ):
		p_now = agent['position']
		if(agent['dirty'][p_now] == True): # Se estiver sujo onde está, THEN limpa
			agent['dirty'][p_now] = False
			state_sequence.append({'agent' : deepcopy(agent), 'action' : 'clean'})
		else: # Else : Move para o lado oposto
			other_side = opposite[p_now]
			agent['position'] = other_side
			state_sequence.append({'agent' : deepcopy(agent), 'action' : 'move to ' + other_side})
	return state_sequence

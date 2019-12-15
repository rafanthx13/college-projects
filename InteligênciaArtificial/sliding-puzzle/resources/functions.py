# Grupo: Rafael Assis e Felipe Francisco - IA UFU 2018-2

# imprimir jogo: A entrada é uma tupla
def print_game(state_game):
	if(len(state_game) != 9):
		print('Tupla Invalida')
	else:
		output = ''
		k = 0
		for i in range(3):
			output += '\t|' 
			for j in range(3):
				output += state_game[j+k] + '|'
			output += '\n'
			k += 3
		print(output, flush=True)

# GUI para Retornar tuple[9] com os dados digitados
def get_start_state():
	# Avisa quais caracteres ainda estao disponiveis para colocar
	def aux_possible_values(list_digits_values, list_valid_values):
		possible_values = []
		output_string = '['
		for valid in list_valid_values:
			if(valid not in list_digits_values):
				possible_values.append(valid)
		for i in possible_values:
			output_string += i + ','
		return output_string[:-1] + ']'
	# Executa processo de Solicitar e receber números
	flag = True
	while(flag):
		valid_values = ['0','1','2','3','4','5','6','7','8']
		output_tuple = []
		get_input = ''
		print('Esquema de indices: (vazio == 0)')
		print('\t|1|2|3|\n\t|4|5|6|\n\t|7|8|9|')
		for i in range(9):
			get_input = input('Digite o numero no espacao ' + str(i+1) + ' :\n==> ' )
			while(True):
				if(get_input not in valid_values):
					print('\nERROR:Valor invalido\n')
					print('Valores ainda Possiveis\n\t' + aux_possible_values(output_tuple, valid_values), '\n')
					
				elif(get_input in output_tuple):
					print('\nERROR: Valor ja foi digitado\n')
					print('Valores ainda Possiveis\n\t' + aux_possible_values(output_tuple, valid_values), '\n')
				else:
					output_tuple.append(get_input)
					break
				get_input = input('Digite o numero no espacao ' + str(i+1) + ' :\n==> ' )
		if('0' not in output_tuple):
			print('Voce nao digitou zero, vai comecar tudo denovo')
			flag = True
		else:
			flag = False
	new_tuple = ['_' if number == '0' else number for number in output_tuple]
	return tuple(new_tuple)

# Get empty Space
def get_empty_space(tuple_state):
	for index in range(len(tuple_state)):
		if(tuple_state[index] == '_'):
			return index
	return None

# Imprime A Sequencia Final
def print_formatted_sequence_total(array_sequence):
	array_sequence['state_sequence'].reverse()
	for state in array_sequence['state_sequence']:
		if(state['action'] == 'Start'):
			print('\t',state['action'])
		else:
			print('\t', str(state['action'][0]), '=>', str(state['action'][1]))
		print(state['state'], 'h:', state['heuristica'], 'fn:', state['f(n)'])
	print('END', 'level: ' + str(array_sequence['level']), 'cost: ' + str(array_sequence['cost']))

# Imprime de forma formatada somente as ações (mais limpo que a verção anterior)
def print_array_actions(array_sequence):
	array_sequence['state_sequence'].reverse()
	count = 0
	string_output = ''
	for state in array_sequence['state_sequence']:
		if(state['action'] == 'Start'):
			string_output += '\t' + state['action'] 
		else:
			string_output += '===> ' + state['action'][0] + ' -> ' + "'" +  state['action'][1] + "' "
			count += 1
		if(count % 5 == 0):
			string_output += '\n\t'
	print(string_output)
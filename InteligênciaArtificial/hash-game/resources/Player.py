import random

infinito = float('inf')
global count_nodes
count_nodes = {'minimax': 0, 'alfabeta': 0}

def h_player(game):
    print(game)
    cont = 0
    
    for i in range(1,4):
        for j in range(1,4):
            if (i,j) in game.acoes():
                print(cont, end = ' ')
                cont += 1
            else:
                print('.', end = ' ')      
        print()
    escolha = int(input('Escolha o int da posicao '))
    	
    jogada = game.acoes()[escolha]
    print(game.move + ' ==>', jogada)
    return jogada

def random_player(game):
	return random.choice(game.acoes()) if game.acoes() else None

def minimax_player(game):
	return minimax_decision(game)

def alfabeta_player(game):
    return alfabeta_decision(game)

def minimax_decision(game):
	
	global count
	count = 0
            
	def max_value(game):
		global count
		if game.test_end():
		    return game.utilidade if game.move =='X' else -game.utilidade
		v = -infinito
		for a in game.acoes():
		    count += 1
		    v = max(v, min_value(game.resultado(a)))
		return v

	def min_value(game):
		global count
		if game.test_end():
		    return -game.utilidade if game.move =='X' else game.utilidade
		v = infinito
		for a in game.acoes():
		    count += 1
		    v = min(v, max_value(game.resultado(a)))
		return v

	best_score = -infinito
	best_action = None

	for a in game.acoes():
		count+=1
		v = min_value(game.resultado(a))
        
		if v > best_score:
		    best_score = v
		    best_action = a
	count_nodes['minimax'] += count
	print('Numero de nos gerados no level', game.level + 1,':', count, best_score)
	return best_action

def alfabeta_decision(game):
   
    global count
    count = 0
        
    def max_value(game,alfa, beta):
        global count
        if game.test_end():
            return game.utilidade if game.move == 'X' else -game.utilidade
        v = -infinito
        for a in game.acoes():
            count += 1
            v = max(v, min_value(game.resultado(a), alfa, beta))
            if v >= beta:
                return v
            alfa = max(alfa, v)
        return v

    def min_value(game,alfa, beta):
        global count
        if game.test_end():
            return -game.utilidade if game.move =='X' else game.utilidade
        v = infinito
        for a in game.acoes():
            count += 1
            v = min(v, max_value(game.resultado(a), alfa, beta) )
            if v <= alfa:
                return v
            beta = min(beta, v)
        return v
    
    best_score = -infinito
    beta = infinito
    best_action = None
    for a in game.acoes():
        count += 1
        v = min_value(game.resultado(a), best_score, beta)
        if v > best_score:
            best_score = v
            best_action = a
    count_nodes['alfabeta'] += count            
    print('Numero de nos gerados no level', game.level + 1, ':', count)
    return best_action


# Deixar Fixo
from resource import functions as f
from resource.Node import Node

acoes=['left','right','clean']
count_nodes = 0

def BUSCA_EM_LARGURA():

    ### Escolhendo o estado inicial
    start_state = f.chose_start_state()								

    no = Node( f.convert_tripla(start_state), 'Start', None, 0, 0)
    ### Printando na tela o estado inicial para confirmar
    print(no)

    if no.target_test():
        return f.print_formatted_sequence(no.sequence_of_action())
    borda = []
    borda.append(no)

    explorado = []
    
    while True:
        if not borda:
            print('Falhou')
            return False
        
        no = borda.pop(0)
        
        explorado.append(no.state)
        
        for acao in acoes :

            filho = no.action_node(acao)

            if not filho.state in explorado:
                global count_nodes
                count_nodes += 1
                if filho.target_test():     
                    return f.print_formatted_sequence(filho.sequence_of_action())
                borda.append(filho) 
def test():
    if __name__ =='__main__':
        BUSCA_EM_LARGURA()
        print('count nos gerados:', count_nodes)
        
test()

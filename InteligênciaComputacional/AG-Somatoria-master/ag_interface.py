# Programa em Python para somatoria
# Grupo: Bruno B, Rafael M. A. (Julho de 2018 Ufu-2018-01)

from tkinter import *
from tkinter import messagebox
from ag_aux_interface import AlgoritmoGenetico, Individuo
from random import randint, random
import matplotlib.pyplot as plt
from math import ceil
import pandas as pd
import time, os

class Application:

    def __init__(self, master = None):
            
        self.ag = AlgoritmoGenetico(100, 10)
        
        self.font = ('Arial', '10')
        self.width = 15

        self.ctTitulo = Frame(master)
        self.ctTitulo['padx'] = 10
        self.ctTitulo['pady'] = 5
        self.ctTitulo.pack()

        self.titulo = Label(self.ctTitulo, text = 'Soma de números', anchor = CENTER)
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        #

        self.ctTermos = Frame(master)
        self.ctTermos['padx'] = 10
        self.ctTermos['pady'] = 5
        self.ctTermos.pack(anchor = W)

        self.lbTermos = Label(self.ctTermos, text = 'Qtde de termos: ', font = self.font, anchor = E, width = self.width, height = 2)
        self.lbTermos.pack(side = LEFT)

        self.etTermos = Entry(self.ctTermos, font = self.font, width = 30)
        self.etTermos.pack(side = LEFT)

        #

        self.ctValor = Frame(master)
        self.ctValor['padx'] = 10
        self.ctValor['pady'] = 5
        self.ctValor.pack(anchor = W)

        self.lbValor = Label(self.ctValor, text = 'Soma esperada: ', font = self.font, anchor = E, width = self.width, height = 2)
        self.lbValor.pack(side = LEFT)

        self.etValor = Entry(self.ctValor, font = self.font, width = 30)
        self.etValor.pack(side = LEFT)
        
        #

        self.ctCalc = Frame(master)
        self.ctCalc['padx'] = 10
        self.ctCalc['pady'] = 20
        self.ctCalc.pack()

        self.btCalc = Button(self.ctCalc, text = 'Calcular', font = self.font, width = 12)
        self.btCalc['command'] = self.Calc
        self.btCalc.pack(side = TOP)

        #
        
        master.mainloop()
        
    def Calc(self):
        global _outside_list
        _outside_list = []

        target = int(self.etValor.get())
        start_length = int(self.etTermos.get())
        mutant_rate = 0.10 # entre [0,1]

        # Insere variaveis staticas
        Individuo.length = start_length
        Individuo.target = target
        Individuo.mutant_rate = mutant_rate

        # Tamnaho da populaçao HardCode
        size_population = 100
        ages = 500 # quantidades de gerações

        # Tempo
        targetime = time.time()

        # Iniciar população
        enviroment = AlgoritmoGenetico(size_population, start_length)
        enviroment.initialize_population()
        enviroment.sort_population()

        # Execução do Fluxograma do AG
        while(enviroment.best_fit.fitness != 0 and enviroment.generation < ages):
                # Nao encontrou ainda, entao, vai fazer até  achar o melhor ou atingir o max
                new_population = []
                # Geranco nova população
                for times in range(ceil(enviroment.size_population/2)):
                        father1_index = enviroment.selection_tournament()
                        father2_index = enviroment.selection_tournament()
                        # garantir diversidade, que os pais sejam diferentes
                        while(father2_index == father1_index):
                                father2_index = enviroment.selection_tournament()
                        # Selecao
                        father1 = enviroment.population[father1_index]
                        father2 = enviroment.population[father2_index]
                        # Crosoover + mutacaço interna
                        son1, son2 = father1.crosoover(father2)
                        new_population.append(son1)
                        new_population.append(son2)
                # Reinserção : gerou uma nova populaçâo
                enviroment.population = new_population
                enviroment.generation += 1
                enviroment.sort_population()

        # Tempo final
        end_time = time.time()
        time_training = round(end_time - targetime, 3)

        # Quando sair por que acho o melhor
        if(enviroment.best_fit.fitness == 0 and enviroment.generation < ages):
                print('\n\tEncontrado uma Resposta Ideal:')
                print(enviroment.best_fit)
        # saiu por que atinigiu o max 
        else:
                print('\n\nChegou ao Limite de epocas:', enviroment.generation)
                print('\n\tA Melhor Resposta das Geracoes:')
                print(enviroment.best_fit) # O melhor das geraçôes, nao presisa ordenar

        print('Sum:', str(sum(enviroment.best_fit.cromossomo)))
        print('Tempo de Treinamento :', time_training, 'segundos', flush = True)

        ### Salvando em CSV dados de estatistias gerais
        labels = ['Target', 'Epochs_Total', 'Time', 'Find_in_Generation', 'Delta_Value_Found']
        file_path = 'general_statistics.csv'
        row = [(tuple([target, ages, str(time_training).replace('.',','), enviroment.best_fit.generation, enviroment.best_fit.fitness] ))]
        df = pd.DataFrame(row, columns = labels)
        if(not os.path.isfile(file_path)):
                df.to_csv(file_path, sep = ';', index = False)
        else:
                df.to_csv(file_path, sep = ';', index = False, mode = 'a', header = False)

        ### Printando mensagem do tk
        printSum = ''
        res = 0
        for i in range(len(enviroment.best_fit.cromossomo)):
            if (i == len(enviroment.best_fit.cromossomo)) or (i == 0):
                printSum = printSum + str(enviroment.best_fit.cromossomo[i])
            else:
                printSum = printSum + '+' + str(enviroment.best_fit.cromossomo[i])
            res = res + enviroment.best_fit.cromossomo[i]
        printSum = printSum + ('=') + str(res)
        if(res == target):
            msg = 'Resultado Encontrado'
        else:
            msg = 'Melhor Resultado das Geracoes. Faltando ' + str(abs(res - target))
        messagebox.showinfo(msg, printSum)

# Exec TK app
root = Tk()
Application(root)
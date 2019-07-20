import pandas as pd
import numpy as np
from random import uniform
import math
import pickle
import os
import time
import timeit
import matplotlib.pyplot as plt

###############################################################
        # Definições de Função

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def degrau(u):
    return 1 if u >= 0 else 0

def sumAttr(features, wj):
    uj = 0
    for feature, value in features.items():
        uj += wj[feature]*value

    return uj

xk  = {}
djk = {}
wj  = []
eta = 0.1

def reading_csv(file_path, array_features):
    # Colocar a media de idade por classe e tornala em inteiro
    # Usada no aaply da coluna de 'Age' para corrigila
    def handler_age(row_age_pclass):
        age = row_age_pclass[0]
        # Se nao tiver Pclass
        if( not ('Pclass' in row_age_pclass)):
                if(pd.isnull(age)):
                        return 31
                else:
                        if(age < 0):
                                return int(np.ceil(age))
                        else:
                                return int(age)
        # Quando tiver Pclass
        pclass = row_age_pclass[1]
        if(pd.isnull(age)):
                if(pclass == 1):
                        return 37
                elif(pclass == 2):
                        return 29
                else:
                        return 24
        else:
                if(age < 0):
                        return int(np.ceil(age))
                else:
                        return int(age)
    # Leitura de CSV
    df = pd.read_csv(file_path, encoding = 'utf-8', sep=',', header = 0)
    # Array de Colunas padrao
    array_default = ['PassengerId', 'Survived']
    array_default.extend(array_features)
    # Tratamento de CSV
    df = df[ array_default ] # Pegando somente as Colunas
    # Tratar cada Coluna
    if('Age' in array_features and not 'Pclass' in array_features):
            df['Age'] = df[ ['Age'] ].apply(handler_age, axis = 1) # Trata a idade
    if('Age' in array_features and 'Pclass' in array_features):
            df['Age'] = df[ ['Age','Pclass'] ].apply(handler_age, axis = 1) # Trata a idade
    if('Sex' in array_features):
            df['Sex'] = pd.get_dummies(df['Sex'], drop_first = True) 
            # Tratar Variavel categorica de Sex ==> 0  e 1 [1 ==> male/ 0 ==> female]
    # Inicializar xk e djk
    xk = {}  # {Passenger_ID => (tuple_features)}
    djk = {} # {Passenger_ID => Survived}
    for index, row in df.iterrows():
            xk[row['PassengerId']] = (row[array_features].to_dict()) # sera das colunas escolhidas
            djk[row['PassengerId']] = row['Survived']
    return xk, djk
	    
def train(xk, djk, eta, features, epocas):
    wj = {}
    list_error = []
    w_best = {}

    for feature in features:
        wj[feature] = uniform(0,1)
        w_best[feature] = None

    period = 0
    best_case = -1
    while True:
        qtd_erro = 0
        qtd_acertos = 0
        for passenger in xk.keys():
            features = xk[passenger]
            uj = sumAttr(features, wj)
            yjk = degrau(uj)
            if yjk != djk[passenger]:
                qtd_erro += 1
                for feature, value in features.items():
                    wj[feature] +=  eta * (djk[passenger] - yjk) * value
            else:
                qtd_acertos += 1
                    
        period += 1
        
        porcentagem_acerto = round((qtd_acertos + 80)/891, 3)
        print(qtd_acertos, '+', qtd_erro, porcentagem_acerto)
        #print(porcentagem_acerto)
        list_error.append(porcentagem_acerto)

        # Fica com melhor
        if(qtd_acertos > best_case):
            for feature in features:
                w_best[feature] = wj[feature]
            best_case = qtd_acertos

        # print(qtd_acertos)
        if(period == epocas):
            return w_best, list_error

###############################################################
    # Execução
print('Rede Neurais - Dataset Titanic - Gerar Porcentagem de Acertos', flush = True)

file_path = ('../dataset/train.csv') # file_path do csv
epocas = 500
array_features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch'] # array de Features usadas

xk, djk = reading_csv(file_path, array_features)

start_time = time.time()

wj, list_error = train(xk, djk, eta, array_features, epocas)

end_time = time.time()
time_training = round(end_time - start_time, 3)

acertos, erros, one_t, one_f, zero_t, zero_f = 0, 0, 0, 0, 0, 0

for passenger_id in xk.keys():
    features = xk[passenger_id]
    uj = sumAttr(features, wj)
    y = degrau(uj)
    if(y == djk[passenger_id]):
        acertos += 1
        if(djk[passenger_id] == 1):
        	one_t += 1
        else:
        	zero_t += 1
    else:
        erros += 1
        if(djk[passenger_id] == 1):
        	one_f += 1
        else:
        	zero_f += 1
        
print('\nExecucao da Rede Treinada:')
print('Acertos :', acertos,'/', 891)
print('Erros :', erros, '/', 891 )
print('Tempo de Treinamento :', time_training, 'segundos')
print('Porcentagem de Acerto :', "{:.2%}".format(acertos/891)) # tranforma em porcentagem com 2 casas decimais

#### Plotar Grafico de Convergencia

fig, axes = plt.subplots(figsize=(8,5))
axes = plt.plot( range(1,epocas+1), list_error)
plt.grid()
plt.xlabel('Épocas')
plt.ylabel('Porcentagem de Acertos')
plt.title('Gráfico de Convergência da Rede Neural')
fig.savefig("convergencia-acertos.png")

# Happy End
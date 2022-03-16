import pandas as pd
import numpy as np
from random import uniform
import math
import pickle
import os
import time
import timeit

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

    for feature in features:
        wj[feature] = uniform(0,1)

    period = 0
    while True:
        for passenger in xk.keys():
            features = xk[passenger]
            uj = sumAttr(features, wj)
            yjk = degrau(uj)
            if yjk != djk[passenger]:
                for feature, value in features.items():
                    wj[feature] +=  eta * (djk[passenger] - yjk) * value
        period += 1
        if(period == epocas):
            return wj

###############################################################
    # Execução
print('Rede Neurais - Dataset Titanic', flush = True)

file_path = ('dataset/train.csv') # file_path do csv
epocas = 2000
array_features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch'] # array de Features usadas

xk, djk = reading_csv(file_path, array_features)

start_time = time.time()

wj = train(xk, djk, eta, array_features, epocas)

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
print('Epocas :', epocas)
print('Acertos :', acertos,'/', 891)
print('Erros :', erros, '/', 891 )
print('Tempo de Treinamento :', time_training, 'segundos')
print('Porcentagem de Acerto :', "{:.2%}".format(acertos/891)) # tranforma em porcentagem com 2 casas decimais

# Print Pesos
print('\nPesos:')
for key, value in wj.items():
    space = ''
    if(key != 'Pclass'):
        space += ' '
    if(key in ['Sex', 'Age']):
        space += '  '
    print(' w[' + key + '] ' + space + '= ', value)


#########################################################################

# Salvando em CSV
labels = ['acertos', 'epocas', 'tempo', 'peso_Pclass', 'peso_Sex', 'peso_Age', 'peso_SibSp', 'peso_Parch']
weights = []
for w in wj.values():
	weights.append(str(w).replace('.',',')) # forma BR aceita pelo Excel
row = []
row.append(tuple([acertos, epocas, str(time_training).replace('.',',')] + weights))
file_path = 'pesos.csv'
df = pd.DataFrame(row, columns = labels)
if(not os.path.isfile(file_path)):
	df.to_csv(file_path, sep = ';', index = False)
else:
	df.to_csv(file_path, sep = ';', index = False, mode = 'a', header = False)

#	Matriz de Confusão
print('\n          MATRIZ DE CONFUSAO ')
print('       (0 = Death, 1 = Survived)')
print('        _________________________')
print('       | 1 PREVISTO | 0 PREVISTO |')
print(' ______|------------|------------|')
print('|1 REAL|',one_t, "{:.2%}".format(one_t/891), '|', one_f,  "{:.2%}".format(one_f/891),'|')
print('|------|------------|------------|')
print('|0 REAL|',zero_f, "{:.2%}".format(zero_f/891), '  |', zero_t,  "{:.2%}".format(zero_t/891),'|')
print(' --------------------------------')

# Salvando em pickle
with open('pesos.pickle', 'wb') as file:
    pickle.dump(wj, file)
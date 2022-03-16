import pandas as pd
import numpy as np
import math
import pickle

###############################################################
        # Definições de Funções

def degrau(u):
    return 1 if u >= 0 else 0

def sumAttr(features, wj):
    uj = 0
    for feature, value in features.items():
        uj += wj[feature]*value
    return uj

def handler_age(row_age_pclass):
    # Colocar a media de idade por classe e tornala em inteiro
    # Usada no aaply da coluna de 'Age' para corrigila
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

def reading_csv(file_path, array_features):
    df = pd.read_csv(file_path, encoding = 'utf-8', sep=',', header = 0)
    # Array de Colunas padrao
    array_default = ['PassengerId']
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
    return xk

def handler_float(row):
    row = row.replace(',','.')
    return float(row)

def search_best_weight(file_path, features):
    const = 'peso_'
    best_rank = 0
    best_row = None
    df  = pd.read_csv('../pesos.csv', sep = ';')
    for row in df.iterrows():
        index, data = row
        row = data.to_dict()
        score = row['acertos']
        if(score > best_rank):
            best_row = row
            best_rank = score
    wj = {}
    for feature in features:
        wj[feature] = handler_float(best_row[const + feature])
    return wj

###############################################################
	# Geração de CSV da Submissão
print('Rede Neurais - Dataset Titanic - Geracao da Submissao', flush = True)

# Constantes
xk  = {}
djk = {}
wj  = None

# Buscar Melhores Pesos # list_w = ['peso_Pclass', 'peso_Sex', 'peso_Age', 'peso_SibSp', 'peso_Parch']
file_path_weight = '../pesos.csv'
features_w = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
wj = search_best_weight(file_path_weight, features_w)

# Ler Arquivo sem o Survive
file_path_csv = '../dataset/test.csv'
xk = reading_csv(file_path_csv, features_w)

# Executar
tuple_list = []
for passenger_id in xk.keys():
    features = xk[passenger_id]
    uj = sumAttr(features, wj)
    predict = degrau(uj)
    tuple_list.append( (passenger_id, predict) )

# Salvando em CSV
labels = ['PassengerId', 'Survived']
file_path_submisison = 'submission.csv'
df = pd.DataFrame(tuple_list, columns = labels)
df.to_csv(file_path_submisison, sep = ',', index = False)

# Fim
print('Happy End')
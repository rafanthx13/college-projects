import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Programa que gera gráfico jointplot para os 5 pesos
# de pesos.csv, mostrando a distribuiççao dos pesos e
# sua relação coma quantidade de acertos

file_path = '../pesos.csv'

# Configs of Pandas
sns.set_style('whitegrid')
sns.set(font_scale = 1.4)

df = pd.read_csv(file_path, sep=';', header = 0)

def handler_float(row):
    row = row.replace(',','.')
    row = "%.2f" % round(float(row),2)
    return float(row)

columns = ['peso_Pclass', 'peso_Sex', 'peso_Age',
 'peso_SibSp', 'peso_Parch']

for coluna in columns:
	name_weight = coluna[5:]
	df[coluna + '_f'] = df[coluna].apply(handler_float)
	chart = sns.jointplot(x = coluna + '_f', y = 'acertos', 
		data = df, kind = 'scatter', dropna = False, stat_func = None)
	chart.fig.suptitle('Peso para o Dado ' + name_weight)
	chart.fig.subplots_adjust(top=0.9)
	chart.savefig('chart' + name_weight + '.png')

print('Happy End')
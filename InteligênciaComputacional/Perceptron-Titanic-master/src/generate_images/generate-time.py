import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def handler_float(row):
    row = row.replace(',','.')
    row = "%.2f" % round(float(row),2)
    return float(row)

######################################

    # Execução
print('Rede Neurais - Gerando Grafico de Tempo x Epocas', flush = True)

file_path = ('../pesos.csv') # file_path do csv
df = pd.read_csv(file_path, sep=';', header = 0)
df['time'] = df['tempo'].apply(handler_float)

list_epocas = []
list_tempo = []

for index, row in df.iterrows():
    #print(row, str(type(row)))
    list_epocas.append(int(row['epocas']))
    list_tempo.append(row['time'])


#### Plotar Grafico de Convergencia

fig, axes = plt.subplots(figsize=(8,5))
# 
axes = plt.plot( list_epocas, list_tempo, 'o', alpha=0.7, lw=2 ,ms=20 ,mfc='orange')
plt.grid()
plt.xlabel('Epocas')
plt.ylabel('Tempo (s)')
plt.title('Gráfico Epocas X Tempo')
fig.savefig("Tempo.png")

# Happy End
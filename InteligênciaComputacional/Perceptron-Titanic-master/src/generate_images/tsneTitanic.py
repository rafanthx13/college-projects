import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.manifold

df = pd.read_csv('../dataset/train_formatted.csv', 
	usecols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Survived'])
df.head()

X = df.as_matrix(columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch'])
Y = df.as_matrix(columns = ['Survived'])
# Normalizando a idade
X[:,2] = (X[:,2] - X[:,2].min())/(X[:,2].max() - X[:,2].min())

# Reduzindo dimensões
tsne = sklearn.manifold.TSNE(n_components = 2, random_state = 0,
 perplexity = 15, n_iter = 2000, n_iter_without_progress = 1000)
matrix_2d = tsne.fit_transform(X)

colors = df.Survived.values
colors = ['G' if i == 1 else 'R' for i in colors]

df_tsne = pd.DataFrame(matrix_2d)
df_tsne['Survived'] = df['Survived']
df_tsne['color'] = colors
df_tsne.columns = ['x', 'y', 'Survived', 'color']

cols = ['Survived', 'color', 'x', 'y']
df_tsne = df_tsne[cols]
df_tsne.head()

# Plotando o gráfico
fig, ax = plt.subplots(figsize = (15,10))
ax.scatter(df_tsne[df_tsne.Survived == 1].x.values, df_tsne[df_tsne.Survived == 1].y.values,
 c = 'green', s = 10, alpha = 0.5, label = 'Survived')
ax.scatter(df_tsne[df_tsne.Survived == 0].x.values, df_tsne[df_tsne.Survived == 0].y.values,
 c = 'red', s = 10, alpha = 0.5, label = 'Died')
ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.legend()
plt.show();

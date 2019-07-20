# Titanic em Python

Trabalho da Disciplina Inteligência Cmputacional. UFU 2018-1.

Grupo:

+ Bruno Borges
+ Eduardo de Freitas
+ Rafael Assis

**Objetivo:** Elaborar rede Neural que preveja se a pessoa sobreviveu ou não ao acidente do titanic tendo com base o dataset da kaggle 

## Dependências

Bibliotecas:

+ pandas; numpy; matplotlib; pickle

execute `Treinamento.py` da pasta `src/`. Na linha de comando `python Treinamento.py` . Tenha todos os pacotes necessarios no python para rodar



## Arquivos de Execução

+ `src/Treinamento.py` : Executa a rede sobre o dataSet e depois testa ela. é o programa Principal
+ `src/generate-images/tsneTitanic.py` : Gera imagem de gráfico tsne que comprova que o problema não é linearmente separável
+ `src/generate-images/generate-time.py`: Gera gráfico de tempo de acordo com os registros salvos em `pesos.csv`. É tempo linear a quantidade de épocas, mas pode variar umpouco de máquina
+ `src/generate-images/generate-joinplot-weights.py`: Gera gráfico de pontos, indicando a influencia de um determinado peso a saida para os 5 atributos de `pesos.csv`
+ `src/src/Interface.py`: Execua `tkinter` , oferece uma interface gráfica para inserir os dados e verificar se sobreviveria ou não. Ele lê `pesos.pickle` e este por sua vez é smepre reescrito/inscrito toda vez que executa `Treinamento.py`
+ `src/generate-images/Convergencia.py`: Gera a convergência do treinamento, por alguma razão nao ta dando valores corretos, por isso foi inserido uma constatne para ficar mais real.
+ `src/old_versions/v_simple_singlelayer/training-network-re.py` : Versão simples do primerio protótipo. Rede Neural Simples. O diferencial é que roda sobre quaisquer combinaçâo das 5 features escolhidas
+ `src/old_version/v_complex_multilayer/training-network.py`: Versão mais complxa, preparada para receber neuronios de frente e de traz (Multi Camada). Tem o erro de que considera os nodos de entrada como neuronios e não é assim, sâo nodos, não neuronios na Input_Layer
+ `src/src/exec-submission.py` : Lê `test.csv` e gera `submission.csv` formatado para ser submetido à kaggle. **Teve acerto de 77,5%**

## Link do DataSet

+ link do data_set: https://www.kaggle.com/c/titanic

## Definição dos Dadosado pra ser submetido a 

| **Variable** | **Definition**                     | **Key**                                        |
| ------------ | ---------------------------------- | ---------------------------------------------- |
| survival     | Survival                           | 0 = No, 1 = Yes                                |
| pclass       | Ticket class                       | 1 = 1st, 2 = 2nd, 3 = 3rd                      |
| sex          | Sex                                |                                                |
| Age          | Age in years                       |                                                |
| sibsp        | Número de Irmãos/conjugues a bordo |                                                |
| parch        | Número de Pais/Filhos a bordo      |                                                |
| ticket       | Ticket number                      |                                                |
| fare         | Passenger fare (tarifa)            |                                                |
| cabin        | Cabin number                       |                                                |
| embarked     | Port of Embarkation                | C = Cherbourg, Q = Queenstown, S = Southampton |

**pclass**: A proxy for socio-economic status (SES)

+ 1st = Upper
+ 2nd = Middle
+ 3rd = Lower

**age**: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

**sibsp**: The dataset defines family relations in this way...

+ Sibling = brother, sister, stepbrother, stepsister
+ Spouse = husband, wife (mistresses and fiancés were ignored)

**parch**: The dataset defines family relations in this way...

+ Parent = mother, father
+ Child = daughter, son, stepdaughter, stepson
+ Some children travelled only with a nanny, therefore parch=0 for them.

---

## Propostas e Ideias de Otimizaçâo e Pesuisas Futuras

+ Gerar script para executar sobre o teste real e enviar
+ Pesquisar pela matriz de confusâo qual é o caso que mais dar erro (Sexo e outros atr)
+ 
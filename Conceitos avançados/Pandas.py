from re import T
import pandas as pd
import numpy as np

# --- Pandas --- # 
# Porque se chama pandas, vem do conjunto de palavras panel data


# --- Items --- #
# Dataframe - Basicamente um conjunto de dados
# Series - Basicamente uma coluna, so que sem o titulo. Mas o nome dela retorna como uma variavel classes

d = {'col1':[2,4,5,6],'col2':[8,8,6,1],'col3':[1,2,3,4],'col4':[4,4,4,4]}

df = pd.DataFrame(d,index=['Item1','Item2','Item1','Item2'])
# Exemplo de dataframe
print(df)
# Exemplo de series
print(df['col1'])
 
df['Col5'] = np.array([1,2,3,4]).astype('int64')

# Como obter uma series de infos de uma vez do sue dataframe
print(df.info())

# Como obter a series dtype de cada coluna
print(df.dtypes)

# Como obter uma serie de infos como media sum min maximo de uma vez
print(df.describe().T)

# Te da os valores do topo do seu dataframe
print(df.head())

#Te da os ultimos valores do dataframe
print(df.tail())


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv('spotify(1).csv', index_col=0) #Aqui estamos definindo que o arquivo ficará guardado no nome "df"
df.sort_values('song_popularity', ascending=False, inplace=True) #Deixa as músicas em ordem de popularidade
df.head(15) #aqui definimos que as primeiras 15 linhas aparecerão (lembrando que começa do 0)

#limpeza
#df.head() #para visualizar o começo do seu dataframe
#df.info() #para obter informações do seu dataframe
#df.describe() #para ver uma descrição mais detalhada 
# essas três servem como uma bússola para saber se estamos limpando da forma certa

df.info() #mostra a quantidade de dados nulos do DataFrame, número total de entradas e datatypes de cada feature

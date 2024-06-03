# %%
import pandas as pd
tabela = pd.read_csv('clientes.csv')
display(tabela)

# %%
display(tabela.info())

# %%
from sklearn.preprocessing import LabelEncoder
codificador = LabelEncoder()
for coluna in tabela.columns: # irá só analisar as colunas da tabela
    if tabela[coluna].dtype == 'object' and coluna != 'score_credito': # SE o tipo da coluna for 'object' e coluna diferente de score...
        tabela[coluna] = codificador.fit_transform (tabela[coluna])
#  Vamo verificar se ocorreu as mudanças,se aparecer tabela é pq n foram modificadas.
for coluna in tabela.columns:
    if tabela[coluna].dtype == 'object' and coluna != 'score_credito':
        display(tabela)  
        # não houve o display da tabela
display(tabela)
        

# %%
# escolhendo quais colunas vamos usar para treinar o modelo de inteligencia artificial
# O 'y'vaiser a coluna que vai ser calculada
# x vai ser todas as colunas que vão ser utulizadas para treinar a inteligencia artificial
x = tabela.drop(['score_credito','id_cliente'],axis=1)
y = tabela['score_credito']

from sklearn.model_selection import train_test_split

# separando os dados de treino e teste,treino vamos dar para os modelos aprederem e teste vamos usar para ver se o modelo aprendeu corretamente
x_treino, x_teste,y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1) 
# Train_test_spli= vai pegar o x e o y,vai embaralhar a base de dados e vai dividir em dados de treino e dados de teste
# 70% treino 30% teste

# %%
from sklearn.ensemble import RandomForestClassifier # importando IA
from sklearn.neighbors import KNeighborsClassifier # importando IA

modelo_arvore = RandomForestClassifier() # modelo de arvore de decisão
modelo_knn = KNeighborsClassifier()      # modelo do vizinho mais próximo

# treinando modelos
modelo_arvore.fit(x_treino,y_treino)
modelo_knn.fit(x_treino,  y_treino)

# %%
# vendo acurácia da IA,a qual ´q uma das métricas para verificar se um modelo é bom em relação ao outro
# Acurácia nada mais é do que a perfomace do modelo,ou seja,vai verificar quantas informações foram verificadas de forma correta
contagem_score = tabela['score_credito'].value_counts()
print(contagem_score['Standard'] / sum(contagem_score)) #chutando tudo em standart

# %%
from sklearn.metrics import accuracy_score
# calculando as previsões
previsao_arvore = modelo_arvore.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste.to_numpy())
#  comparando as previsões com o y_teste
# esse score queremos o maior(maior acurácia, mas também tem que ser maior do que o chute de tudo standart)
print(accuracy_score(y_teste, previsao_arvore))
print(accuracy_score(y_teste, previsao_knn))


# %%
novos_clientes = pd.read_csv('novos_clientes.csv')
display(novos_clientes)
novos_clientes['profissao'] = codificador.fit_transform(novos_clientes['profissao'])
novos_clientes['mix_credito'] = codificador.fit_transform(novos_clientes['mix_credito'])
novos_clientes['comportamento_pagamento'] = codificador.fit_transform(novos_clientes['comportamento_pagamento'])



previsao = modelo_arvore.predict(novos_clientes)
print(previsao)



# %%
import pandas as pd
tabela = pd.read_csv('cancelamentos.csv') # importando banco de dados
tabela = tabela.drop('CustomerID', axis=1) # informação ''inútil'' Vai retirar para começar o análise
#o '.drop' serve para retirar uma coluna da tabela
display(tabela)

# %%
# REMOVENDO INFORMAÇÕES VAZIAS
display(tabela.info()) 
tabela = tabela.dropna() # vai remover as informações vazias
display(tabela.info()) # vai mostrar as informações da tabela

# %%
#VERIFIFCANDO A TAXA DE CANCELAMENTO
#quantas pessoas cancelaram e não cancelaram
display(tabela['cancelou'].value_counts())
display(tabela['cancelou'].value_counts(normalize=True).map('{:.1%}'.format)) # EM PORCENTAGEM e formatado
display(tabela['cancelou'].value_counts(normalize=True)) # EM PORCENTAGEM n/ formatado

# %%
# VERIFICANDO CANCELAMENTO POR CONTRATO
display(tabela['duracao_contrato'].value_counts(normalize=True)) #EM PORCENTAGEM
display(tabela['duracao_contrato'].value_counts(normalize=True).map('{:.1%}'.format)) # EM PORCENTAGEM E FORMATADO
display(tabela['duracao_contrato'].value_counts()) # EM NÚMERO

# %%
# ANALISANDO CONTRATO MENSAL
display(tabela.groupby('duracao_contrato').mean(numeric_only=True)) # o GROUPBY vai realizar o agrupamento e o 'mean' vai realizar a media
# NUMERIC_ONLY=True vai fazer a média só dos números

# %%
#DESCOBRINDO QUE O CONTRATO MENSAL É RUIM,vamos remover e continuar analisando
tabela = tabela[tabela['duracao_contrato']!='Monthly']
display(tabela)
display(tabela['cancelou'].value_counts())
display(tabela['cancelou'].value_counts(normalize=True).map('{:.1%}'.format))

# %%
# ANALISE DE ASSINATURAS
display(tabela['assinatura'].value_counts())
display(tabela['assinatura'].value_counts(normalize=True)) # contagem dos valores na coluna das assinaturas
display(tabela.groupby('assinatura').mean(numeric_only=True)) # agrupar informações por assinatura e obter média

# %%
import plotly.express as px
import nbformat as nbformat
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna,color='cancelou',width=600) 
    display(grafico)

# %%
tabela = tabela[tabela['ligacoes_callcenter']<5] #REMOVENDO
tabela = tabela[tabela['dias_atraso']<=20] # REMOVENDO
display(tabela)
display(tabela['cancelou'].value_counts()) #QUEM CANCELOU EXCLUINDO OS VALORES A CIMA
display(tabela['cancelou'].value_counts(normalize=True).map('{:.1%}'.format))



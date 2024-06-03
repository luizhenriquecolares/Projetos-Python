# %% [markdown]
# # Comparando, Tratando e Mesclando DataFrames
# 
# ## Objetivo
# 
# Vamos modificar os IDs para os nomes dos produtos, dos clientes e das lojas, para nossas análises ficarem mais intuitivas futuramente. Para isso, vamos criar um data frame com todos os detalhes.
# 
# - Usaremos o método merge para isso e, depois se quisermos, podemos pegar apenas as colunas que queremos do dataframe final.

# %% [markdown]
# ### Criando nossos dataframes

# %%
import pandas as pd

#às vezes precisaremos mudar o encoding. Possiveis valores para testar:
#encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'
vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';',encoding='latin1')
lojas_df = pd.read_csv('Contoso - Lojas.csv',sep=';',encoding='latin1')
clientes_df = pd.read_csv('Contoso - Clientes.csv',sep=';',encoding='latin1')
produtos_df = pd.read_csv('Contoso - Cadastro Produtos.csv',sep=';',encoding='latin1')


#usaremos o display para ver todos os dataframes

display(vendas_df)
display(lojas_df)
display(clientes_df)
display(produtos_df)

# %% [markdown]
# ### Vamos tirar as colunas inúteis do clientes_df ou pegar apenas as colunas que quisermos

# %%
.drop([coluna1, coluna2, coluna3]) -> retira as colunas: coluna1, coluna2, coluna3

# %%
clientes_df = clientes_df.drop(['Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10'],axis=1)



# %%
clientes_df = clientes_df[['ÿID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'ï»¿Nome da Marca']]
lojas_df = lojas_df[['ÿID Loja', 'Nome da Loja']]

# Esta selocionando apenas as colunas que irão ser utilizadas para o análise de dados

# %% [markdown]
# ### Agora vamos juntar os dataframes para ter 1 único dataframe com tudo "bonito"

# %%
novo_dataframe = dataframe1.merge(dataframe2, on='coluna')

objetivo = Vai juntar dois dataframes por meio de uma coluna em comum.

# %% [markdown]
# - Obs: O merge precisa das colunas com o mesmo nome para funcionar. Se não tiver, você precisa alterar o nome da coluna com o .rename

# %%
dataframe.rename({'coluna1': 'novo_coluna_1'})


# %%
# Alterando nome do id loja;
lojas_df = lojas_df.rename({'ÿID Loja':'ID Loja'},axis=1)

# Alterando ID cliente:
clientes_df = clientes_df.rename({'ÿID Cliente' : 'ID Cliente'},axis=1)
display(vendas_df)

# %%
#juntando os dataframes
display(vendas_df)
display(produtos_df)
display(lojas_df)
display(clientes_df)

vendas_df = vendas_df.merge(produtos_df,on='ID Produto')
vendas_df = vendas_df.merge(lojas_df,on='ID Loja')
vendas_df = vendas_df.merge(clientes_df,on='ID Cliente')

#exibindo o dataframe final
display(vendas_df)


# %%
#vamos renomear o e-mail para ficar claro que é do cliente
vendas_df = vendas_df.rename({'E-mail' : 'E-mail Clientes'},axis=1)
display(vendas_df)

# %% [markdown]
# ### Agora podemos começar as análises

# %%
frequencia_clientes = vendas_df['E-mail Clientes'].value_counts() # Contar a frequencia de valores unicos em uma coluna especifica
display(frequencia_clientes.head()) # Vai mostrar os 5 primeiros valores
frequencia_clientes[:5].plot(figsize=(30, 5))

# %%
# Loja que mais vendeu:
display(vendas_df)
vendas_lojas = vendas_df.groupby(['Nome da Loja']).sum()
display(vendas_lojas)
qtd_vendida = vendas_lojas[['Quantidade Vendida']] 
vendas_lojas['Total'] = vendas_lojas['Quantidade Vendida'] - vendas_lojas['Quantidade Devolvida']
vendas_lojas = vendas_lojas[['Total']]
display(vendas_lojas)

# %%
# Ordenar um dateframe
vendas_lojas = vendas_lojas.sort_values(['Total'],ascending=False) # Vai mostrar do maior para o menor
# dataframe = dataframe.sort_values('lista que tu quer ordenar',ascending=False)
display(vendas_lojas[:5]) #O .head() pode ser utilizado para o top5, quando é passado sem prãmetro ele mostra os 5 valores
display(vendas_lojas)

# %%
# Mair valor pelo max()

maior_venda = vendas_lojas['Quantidade Vendida'].max()
print(maior_venda)

# Indice do maior valor pelo .idxmax()
melhor_loja= vendas_lojas['Quantidade Vendida'].idxmax()
print(melhor_loja)

# %%
# Qual produto menos vendeu
menor_valor = vendas_lojas['Quantidade Vendida'].min()
loja_ruim = vendas_lojas['Quantidade Vendida'].idxmin()
print(loja_ruim, menor_valor)


# %% [markdown]
# ### Quantidade em % de vendas que foi devolvido:

# %%
# Quantidade em % de vendas que foi de volvido:
qtd_vendida = vendas_df['Quantidade Vendida'].sum()
qtd_devolvida = vendas_df['Quantidade Devolvida'].sum()
print('{:.2%}'.format(qtd_devolvida / qtd_vendida))

# %% [markdown]
# ### Vamos realizar a analise de apenas uma loja.Queremos filtrar apenas os itens da loja Contoso Europe Online e saber % de devolução dessa loja.
# 

# %%


vendas_lojacontoso = vendas_df[vendas_df['ID Loja'] == 306]
display(vendas_lojacontoso)
qtd_de_venda = vendas_lojacontoso['Quantidade Vendida'].sum()
qtd_devolucao = vendas_lojacontoso['Quantidade Devolvida'].sum()
print('{:.2%}'.format(qtd_devolucao / qtd_de_venda))

# %% [markdown]
# ### Desafio: e se eu quisesse criar uma tabela apenas com as vendas da loja Contoso Europe Online e que não tiveram nenhuma devolução.Quero criar essa tabela e saber quantas vendas são.

# %%
tabela_analise = vendas_df[(vendas_df['ID Loja'] == 306) & (vendas_df['Quantidade Devolvida'] == 0)]
display(tabela_analise)

# %%
tabela_analise = tabela_analise[(tabela_analise['ID Promocao'] == 10) & (tabela_analise['ID Canal'] == 4)] 
display(tabela_analise)

# %% [markdown]
# ### Agora, e se quisermos acrescentar uma coluna com o mês, o dia e o ano de cada venda(e não só a data completa)
# 

# %%
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'], format='%d/%m/%Y')
vendas_df['Dia'] = vendas_df['Data da Venda'].dt.day
vendas_df['mês'] = vendas_df['Data da Venda'].dt.month
vendas_df['ano'] = vendas_df['Data da Venda'].dt.year
display(vendas_df)



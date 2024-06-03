# %%
import pandas as pd 

tabela =  pd.read_excel('Vendas.xlsx')
display(tabela.drop('Data',axis=1))


# %%
# a empresa quer aumentar suas vendas
#analisar tabela
# ver o faturamento total e o de cada loja
faturamento_total = tabela['Valor Final'].sum()
display(faturamento_total)



# %%
faturamento_por_loja = tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
# quando é mais de uma informação(ID loja, valor final) vai precisar de mais um []
#'groupby() vai agrupar as informações da coluna (organizar por linha)
# O '.sum' vai somar o valor final de cada informação(loja)
display(faturamento_por_loja)
# descobriu a loja que vende mais
#pq ta vendendo mais?



# %%
# pq a loja Iguatemi Campinas ta vendendo mais? Vamos analisar os produtos que sao mais vendidos
faturamento_por_produto = tabela[['ID Loja', 'Produto', 'Valor Final']].groupby(['ID Loja','Produto']).sum()
# quando é mais de uma informação(ID loja, valor final) vai precisar de mais um []
# groupby() vai agrupar as informações da coluna (organizar por linha)
# O '.sum' vai somar o valor final de cada informação(produto)

# Melhor não agrupar valores,é bom deixar pra somar e se tomar de base para a análise de dados

display(faturamento_por_produto)



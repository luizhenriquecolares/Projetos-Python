# %% [markdown]
# ## Exercício Desafio
# 
# - Digamos que seu chefe pediu para você um relatório da análise dos salários da unidade de San Francisco da empresa. O objetivo dele é entender:
# 
# 1. Qual foi a evolução do salário médio ao longo dos anos (TotalPay e TotalPayBenefits)
# 2. Quantos funcionários tivemos ao longo dos anos
# 3. Qual foi a evolução do total gasto com salário ao longo dos anos (TotalPayBenefits)
# 
# - Base de Dados a ser usada: salarios.sqlite

# %% [markdown]
# ### Importação da Base de Dados

# %%
import sqlite3
import pandas as pd
conexao1 = sqlite3.connect('salarios.sqlite')
tabela_salarios = pd.read_sql('SELECT * FROM salaries', conexao1)
display(tabela_salarios)
conexao1.close()

# %%
import pyodbc
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
            "Server=localhost;" #Localhost é por que o banco de dados ja está no computador 
            "Database=salarios.sqlite;")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute('SELECT * FROM Salaries')
valores = cursor.fetchall()
descricao = cursor.description
print(valores[:10])
print(descricao)


cursor.close()
conexao.close()


# %%
import  pandas as pd
colunas = [tupla[0] for tupla in descricao]
tabela = pd.DataFrame.from_records(valores,columns=colunas)
display(tabela)


# %% [markdown]
# ### Análise de Dados

# %%
# garantindo que estamos só com San Francisco
# tabela_editada = tabela 
tabela = tabela.loc[tabela['Agency'] == 'San Francisco', :]
display(tabela)
print(tabela.info())

# %% [markdown]
# ##### 1. Qual foi a evolução do salário médio ao longo dos anos

# %%

tabel_salarial = tabela[['TotalPay','TotalPayBenefits', 'Year']].groupby("Year").mean()
display(tabel_salarial[['TotalPay','TotalPayBenefits']])


# %% [markdown]
# ##### 2. Quantos funcionários tivemos ao longo dos anos

# %%
tabela_funcionario = tabela[['Id','Year']].groupby('Year').count()
tabela_funcionario = tabela_funcionario.rename(columns={'Id':'Qtd Funcionários'})
display(tabela_funcionario)

# %% [markdown]
# ##### 3. Qual foi a evolução do total gasto com salário ao longo dos anos

# %%
def formatar_valor(valor):
    return 'R${:,.2f}'.format(valor)

tabela_total_gasto = tabela[['TotalPay','TotalPayBenefits', 'Year']].groupby('Year').sum()

tabela_total_gasto['TotalPay'] = tabela_total_gasto['TotalPay'].apply(formatar_valor) # Vai aplicar a função em cada item da tabela
tabela_total_gasto['TotalPayBenefits'] = tabela_total_gasto['TotalPayBenefits'].map(formatar_valor) # Pode se aplicar o map tbm,vai realizar mesma funçao do apply
display(tabela_total_gasto)



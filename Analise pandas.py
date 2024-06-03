# %% [markdown]
# # Exercício - Mini Projeto de Análise de Dados
# 
# Vamos fazer um exercício completo de pandas para um miniprojeto de análise de dados.
# 
# Esse exercício vai obrigar a gente a usar boa parte dos conhecimento de pandas e até de outros módulos que já aprendemos ao longo do curso.
# 
# ### O que temos?
# 
# Temos os dados de 2019 de uma empresa de prestação de serviços. 
# 
# - CadastroFuncionarios
# - CadastroClientes
# - BaseServiçosPrestados
# 
# Obs1: Para ler arquivos csv, temos o read_csv<br>
# Obs2: Para ler arquivos xlsx (arquivos em excel normais, que não são padrão csv), temos o read_excel
# 
# ### O que queremos saber/fazer?
# 
# 1. Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa? <br>
#     Sugestão: calcule o salário total de cada funcionário, salário + benefícios + impostos, depois some todos os salários
#     
#     
# 2. Qual foi o faturamento da empresa?<br>
#     Sugestão: calcule o faturamento total de cada serviço e depois some o faturamento de todos
#     
#     
# 3. Qual o % de funcionários que já fechou algum contrato?<br>
#     Sugestão: na base de serviços temos o funcionário que fechou cada serviço. Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.<br>
#     . Na base de funcionários temos uma lista com todos os funcionários<br>
#     . Queremos calcular Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais<br>
#     . Para calcular a qtde de funcionários que fecharam algum serviço, use a base de serviços e conte quantos funcionários tem ali. Mas lembre-se, cada funcionário só pode ser contado uma única vez.<br><br>
#     Dica: se você aplicar o método .unique() em uma variável que é apenas 1 coluna de um dataframe, ele vai excluir todos os valores duplicados daquela coluna.<br>
#     Ex: unicos_colunaA = dataframe['colunaA'].unique() te dá como resposta uma lista com todos os itens da colunaA aparecendo uma única vez. Todos os valores repetidos da colunaA são excluidos da variável unicos_colunaA 
#     
#     
# 4. Calcule o total de contratos que cada área da empresa já fechou
# 
# 
# 5. Calcule o total de funcionários por área
# 
# 
# 6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?<br>
#     Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()
# 
# Obs: Lembrando as opções mais usuais de encoding:<br>
# encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'
# 
# Observação Importante: Se o seu código der um erro na hora de importar os arquivos:<br>
# - CadastroClientes.csv
# - CadastroFuncionarios.csv
# 
# Use separador ";" (ponto e vírgula) para resolver

# %%
import pandas as pd
tabela_clientes = pd.read_csv('CadastroClientes.csv',sep=';',decimal=',')
display(tabela_clientes)

tabela_funcionarios = pd.read_csv('CadastroFuncionarios.csv',sep=';',decimal=',') # Transfornou os numeros com vírgulo no padrao python
tabela_funcionarios = tabela_funcionarios.drop(['Estado Civil','Cargo'],axis=1)
display(tabela_funcionarios)

tabela_serviço = pd.read_excel('BaseServiçosPrestados.xlsx')
display(tabela_serviço)


# %% [markdown]
# ### Folha salarial.

# %%
tabela_funcionarios['Salario Total'] = tabela_funcionarios['Salario Base'] + tabela_funcionarios['Impostos'] + tabela_funcionarios['Beneficios'] + tabela_funcionarios['VT'] + tabela_funcionarios['VR']
display(tabela_funcionarios)
print('A folha salarial da empresa é igual a : R${:,.2f}'.format(sum(tabela_funcionarios['Salario Total'])))

# %% [markdown]
# ### Faturamento da empresa
# 

# %%
tabela_faturamento = tabela_serviço[['Tempo Total de Contrato (Meses)','ID Cliente']].merge(tabela_clientes[['ID Cliente','Valor Contrato Mensal']],on='ID Cliente')
tabela_faturamento['Faturamento Total'] = tabela_faturamento['Tempo Total de Contrato (Meses)'] * tabela_faturamento['Valor Contrato Mensal']
print('Faturamento total da empresa foi de : R${:,.2f}'.format(sum(tabela_faturamento['Faturamento Total'])))
display(tabela_faturamento)

# %% [markdown]
# ### Percentual de funcionários que fecharam contratos.
# 

# %%
func_contrato = len(tabela_serviço['ID Funcionário'].unique()) # O .unique() serve para pegar os valores unicos
total_func = len(tabela_funcionarios['ID Funcionário'])
print('Funcionarios que fecharam contrato {:.2%}'.format((func_contrato / total_func)))
print(total_func)

# %% [markdown]
# ### Qtde de Contratos por area

# %%
contratos_area = tabela_serviço[['ID Funcionário']].merge(tabela_funcionarios[['ID Funcionário','Area']],on='ID Funcionário')
contratos_area_qtd = contratos_area['Area'].value_counts()
display(contratos_area_qtd)

# %% [markdown]
# ### Funcionarios por area

# %%
funcionarios_area = tabela_funcionarios['Area'].value_counts()
display(funcionarios_area)

# %% [markdown]
# ### Ticket medio mensal
# 

# %%
ticket_medios = tabela_clientes['Valor Contrato Mensal']
print('{:.2f}'.format(ticket_medios.mean()))



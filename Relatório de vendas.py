
# %% [markdown]
# ## Relatório de vendas

# %% [markdown]
# ### Primeira versão do relatório de vendas

# %% [markdown]
# Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa.
# O usuário deve digitar o nome do vendedor e suas vendas, e o programa deve manter o controle
# do total e da média de vendas para cada vendedor.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar os dados de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
# 
# Exemplo de saída:
#     
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 100
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 200
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 300
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 400.0, Média de vendas = R$ 200.0
# Maria: Total de vendas = R$ 200.0, Média de vendas = R$ 200.0
# ```
# 
# Dica: use o método sum() para calcular o total de vendas e o método len() para calcular o número de vendas.
# 

# %%
# solução

dados_vendas = {}
while True:
    nome = input("Digite o nome do vendedor (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    vendas = float(input("Digite as vendas: "))
    if nome not in dados_vendas:
        dados_vendas[nome] = [vendas]
    else:
        dados_vendas[nome].append(vendas)

for nome, vendas in dados_vendas.items():
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    print(f"{nome}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")


# %% [markdown]
# ### Segunda versão do relatório de vendas
# 

# %% [markdown]
# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
# 
# Além disso, ao invés de armazenar cada venda em uma lista para cada vendedor, armazene
# o total de vendas e a quantidade de vendas em um dicionário. Por exemplo, se o usuário
# digitar "João" e "1000" para vendas, o dicionário deve ficar assim:
# 
# ```python
# {'João': {'total_vendas': 1000, 'quantidade_vendas': 1}}
# ```
# 
# Se, após, o usuário digitar "João" e "2000" para vendas, o dicionário deve ficar assim:
# 
# ```python
# {'João': {'total_vendas': 3000, 'quantidade_vendas': 2}}
# ```
# 
# Perceba como o total de vendas de João aumentou em 2000, assim como a quantidade aumentou em uma unidade.
# 
# Ao final, mostre o total de vendas e a média de vendas de cada vendedor.
# 
# Exemplo de saída:
# 
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 1000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 3000
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 3000.00, Média de vendas = R$ 1500.00
# Maria: Total de vendas = R$ 5000.00, Média de vendas = R$ 2500.00
# ```
# 

# %%
# solução

dados_vendas = {}
while True:
    nome = input("Digite o nome do vendedor (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    try:
        vendas = float(input("Digite as vendas: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para vendas.")
        continue
    if nome not in dados_vendas:
        dados_vendas[nome] = {'total_vendas': vendas, 'quantidade_vendas': 1}
    else:
        dados_vendas[nome]['total_vendas'] += vendas
        dados_vendas[nome]['quantidade_vendas'] += 1

for nome, dados in dados_vendas.items():
    total_vendas = dados['total_vendas']
    media_vendas = total_vendas / dados['quantidade_vendas']
    print(f"{nome}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")


# %% [markdown]
# ### Terceira versão do relatório de vendas

# %% [markdown]
#  Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações: `solicitar_nome_vendedor`, `solicitar_vendas` e `atualizar_dados` e `print_dados`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.

# %%
# solução


def solicitar_nome_vendedor():
    return input("Digite o nome do vendedor (ou 'sair' para sair): ").lower()


def solicitar_vendas():
    try:
        return float(input("Digite as vendas: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para vendas.")
        return None

    
def atualizar_dados(dados_vendas, nome, vendas):
    if nome not in dados_vendas:
        dados_vendas[nome] = {'total_vendas': vendas, 'quantidade_vendas': 1}
    else:
        dados_vendas[nome]['total_vendas'] += vendas
        dados_vendas[nome]['quantidade_vendas'] += 1
        

def print_dados(dados_vendas):
    for nome, dados in dados_vendas.items():
        total_vendas = dados['total_vendas']
        media_vendas = total_vendas / dados['quantidade_vendas']
        print(f"{nome}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")
        

def main():
    dados_vendas = {}
    while True:
        nome = solicitar_nome_vendedor()
        if nome == 'sair':
            break
        vendas = solicitar_vendas()
        if vendas is None:
            continue
        atualizar_dados(dados_vendas, nome, vendas)
    print_dados(dados_vendas)

if __name__ == "__main__":
    main()






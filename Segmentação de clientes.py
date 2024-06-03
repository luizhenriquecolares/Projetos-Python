
# %% [markdown]
# ## Segmentação de clientes

# %% [markdown]
# ### Primeira versão da segmentação de clientes

# %% [markdown]
# Escreva um programa que segmenta clientes com base em suas compras totais.
# O usuário deve digitar o nome do cliente e suas compras totais, e o programa
# deve atribuir cada cliente a um segmento: 'Bronze' para compras de até R\\$ 1000,
# 'Prata' para compras de até R\\$ 5000 e 'Ouro' para compras acima de R\\$ 5000.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar os clientes e seus segmentos.
# 2. Crie um loop infinito que solicite ao usuário o nome do cliente e suas compras totais.
# 3. Dentro do loop, use uma declaração if para atribuir o segmento apropriado ao cliente.
# 4. Se o usuário digitar 'sair' para o nome do cliente, encerre o loop usando break.
# 5. Fora do loop, use um loop for para imprimir o nome e o segmento de cada cliente.
# 
# Exemplo de saída:
#     
# ```
# Digite o nome do cliente (ou 'sair' para sair): João
# Digite o total de compras: 100
# Digite o nome do cliente (ou 'sair' para sair): Maria
# Digite o total de compras: 2000
# Digite o nome do cliente (ou 'sair' para sair): José
# Digite o total de compras: 6000
# Digite o nome do cliente (ou 'sair' para sair): sair
# João: Segmento do Cliente = Bronze
# Maria: Segmento do Cliente = Prata
# José: Segmento do Cliente = Ouro
# ```
# 

# %%
# solução

clientes = {}
while True:
    nome = input("Digite o nome do cliente (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    compras = float(input("Digite o total de compras: "))
    if compras <= 1000:
        segmento = 'Bronze'
    elif compras <= 5000:
        segmento = 'Prata'
    else:
        segmento = 'Ouro'
    clientes[nome] = segmento
print(clientes)
for nome, segmento in clientes.items():
    print(f"{nome}: Segmento do Cliente = {segmento}")


# %% [markdown]
# ### Segunda versão da segmentação de clientes
# 

# %% [markdown]
# 
# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para compras, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para compras." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
# 
# Além disso, ao invés de deixar os limites de compras fixos no programa, armazene-os em uma
# lista de tuplas. Por exemplo:
# 
# ```python
# segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
# ``` 
# 
# Assim, outros segmentos podem ser adicionados facilmente. O primeiro elemento da tupla é o
# limite de compras e o segundo é o nome do segmento. O último elemento da lista é uma tupla
# com limite `float('inf')`, que representa o segmento Ouro. Isso significa que, se o valor de
# compras for maior que todos os limites, o segmento será Ouro.
# 
# Depois, percorra essa lista e, para cada tupla, verifique se o valor de compras é menor ou igual
# ao limite. Se for, armazene o segmento em um dicionário. Por exemplo, se o usuário digitar
# "João" e "500" para compras, o dicionário deve ficar assim:
# `{'João': 'Bronze'}`
# 

# %%
# solução

segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
clientes = {}
while True:
    nome = input("Digite o nome do cliente (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    try:
        compras = float(input("Digite o total de compras: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para compras.")
        continue
    for limite, segmento in segmentos:
        if compras <= limite:
            clientes[nome] = segmento
            break

for nome, segmento in clientes.items():
    print(f"{nome}: Segmento do Cliente = {segmento}")


# %% [markdown]
# ### Terceira versão da segmentação de clientes

# %% [markdown]
# Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações: `solicitar_nome_cliente`, `solicitar_total_compras` e `atribuir_segmento` e `print_segmento_por_cliente`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções. Além disso, normalize que todos os nomes sejam armazenados em letras minúsculas.

# %%
# solução


def solicitar_nome_cliente():
    return input("Digite o nome do cliente (ou 'sair' para sair): ").lower()


def solicitar_total_compras():
    try:
        return float(input("Digite o total de compras: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para compras.")
        return None
    

def atribuir_segmento(compras, segmentos):
    for limite, segmento in segmentos:
        if compras <= limite:
            return segmento
        

def print_segmento_por_cliente(clientes):
    for nome, segmento in clientes.items():
        print(f"{nome}: Segmento do Cliente = {segmento}")
        

def main():
    segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
    clientes = {}
    while True:
        nome = solicitar_nome_cliente()
        if nome == 'sair':
            break
        compras = solicitar_total_compras()
        if compras is None:
            continue
        clientes[nome] = atribuir_segmento(compras, segmentos)
    print_segmento_por_cliente(clientes)

    
if __name__ == "__main__":
    main()







# %% [markdown]
# # Criando um aplicativo de compras
# - salvar a lista em um arquivo 
# - carregar uma lista existente 
# - gerenciar múltiplas listas de compras, cada uma em um arquivo diferente 
# - salvar a lista atual em um arquivo ou sair sem salvar
# 
# Organize o programa em funções. Cada função deve ter uma única responsabilidade. O programa deve ter:
# 
# - função `main` que chama as outras funções 
# - um menu que permite ao usuário escolher uma opção 
# - uma função para cada opção do menu 
# - uma função para cada operação que pode ser realizada na lista de compras

# %%
import json
import time
import os


def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade
    pass

def remover_item(compras, item):
    if item in compras:
        del compras[item]
    else:
        print('Item não existe')
    pass

def visualizar_compras(compras):
    for item, quantidade in compras.items():
        print(f'{item}:{quantidade}')
    print()
    print('Pressione enter para continuar')
    input()
    pass

def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo: # O 'w' significa que esta escrevendo um arquivo
        json.dump(compras, arquivo) #Nome do que voce vai jogar no arquivo(no caso o dicionario), e onde vai ser jogado(no arquivo que foi criado)
    pass

def carregar_compras(nome_arquivo):
    with open(nome_arquivo,'r') as arquivo: # O 'r' significa que está lendo um arquivo(read)
        return json.load(arquivo)
    pass

def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear' )
        print('1 adicionar item')
        print('2 remover item')
        print('3 visualizar lista')
        print('4 salvar e sair')
        print('5 sair sem salvar')
        escolha = int(input('escolha uma opção :'))

        if escolha == 1:
            item = input('digie o nome do item:')
            quantidade = int(input('digite a quantidade:'))
            adicionar_item(compras, item, quantidade)
            
        elif escolha == 2:
            item = input('digie o nome do item:')
            if item in compras:
                remover_item(compras, item)
            else:
                print('Item não está cadastrado')
            pass
        elif escolha == 3:
            visualizar_compras(compras)
            pass
        elif escolha == 4:
            if nome_arquivo  is None:
                nome_arquivo = input('Digite o nome do arquivo:')
            if not nome_arquivo.endswith('.json'):
                nome_arquivo += '.json'
            salvar_compras(compras,nome_arquivo)
            break
        elif escolha == 5:
            break
        else:
            print('Opção inválida')
            time.sleep(1)
    

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear' ) # esse comando faz com que limpe a tela de exibição(toda vez que inicia o loop)
        print('1 criar uma nova lista de compras')
        print('2 carregar uma lista existente')
        print('3 sair')
        escolha = int(input('Escolha uma função :'))

        if escolha == 1:
            compras = {} # dicionário onde as listas e arquivos vão ser atribuídos 
            gerenciar_compras(compras)
        elif escolha == 2:
            print('lista e arquivos:')
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith('.json')]
            if not arquivos:
                print('Nenhuma lista encontrada')
                time.sleep(2)
                continue
            for i,arquivo in enumerate(arquivos, 1): # Vai começar com o numero 1
                print(f'{i} {arquivo}')
            escolha= int(input('escolha uma lista para carregar(0 se nenhuma):'))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print('opção inválida')
                time.sleep(1)
            nome_arquivo = arquivos[escolha-1]  # Pois começa com 0,ent o numero colocado sempre vai ser -1
            compras = carregar_compras(nome_arquivo) 
            gerenciar_compras(nome_arquivo)
        elif escolha == 3:
            break
        else:
            print('Opção inválida')
            time.sleep(1)

if __name__ == '__main__':  #Funcionalidade interna do python,atribuindo como arquivo principal(chamando a função main)
    main()



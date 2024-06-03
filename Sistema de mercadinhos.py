# %% [markdown]
# # Exercícios de fixação 

# %% [markdown]
# A seguir, você encontrará alguns exercícios para fixar os conceitos aprendidos no curso até agora. Os exercícios estão divididos por exemplos práticos da vida real:
# 
# - lista de compras
# - previsão de vendas
# - relatório de vendas
# - segmentação de clientes
# - analisador de texto




# %%
# solução
    
    
def adicionar_item(lista_compras):
    item = input("Digite um item: ").lower()
    quantidade = int(input("Digite a quantidade: "))
    if item in lista_compras:
        lista_compras[item] += quantidade
    else:
        lista_compras[item] = quantidade

        
def remover_item(lista_compras):
    item = input("Digite um item: ").lower()
    if item in lista_compras:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade >= lista_compras[item]:
            del lista_compras[item]
        else:
            lista_compras[item] -= quantidade
    else:
        print("Item não está na lista de compras")
        

def ver_lista(lista_compras):
    for item, quantidade in lista_compras.items():
        print(f"{item}: {quantidade}")
        

def main():
    
    lista_compras = {}  
    
    while True:
        print()
        
        print("1 Adicionar item")
        print("2 Remover item")
        print("3 Ver lista")
        print("4 Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_item(lista_compras)
        elif escolha == '2':
            remover_item(lista_compras)
        elif escolha == '3':
            ver_lista(lista_compras)
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()





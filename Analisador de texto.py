
# %% [markdown]
# ## Analisador de texto

# %% [markdown]
# Crie um programa que analise um texto fornecido pelo usuário.
# O programa deve contar o número de palavras (independentemente se há repetição ou não),
# a quantidade de cada palavra e a
# quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras.
# Não se preocupe com pontuação e espaços ao contar palavras.
# 
# O programa deve conter uma função chamada `analisar_texto` que recebe o texto
# como parâmetro e retorna a contagem de palavras, a frequência de palavras e a
# frequência de letras.
# 
# Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve
# imprimir:
#     
# ```
# Contagem de palavras: 8
# Frequência de palavras: {'Olá': 2, 'mundo!': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste.': 1, 'novamente.': 1}
# Frequência de letras: {'o': 4, 'l': 2, 'á': 2, 'm': 3, 'u': 2, 'n': 3, 'd': 1, '!': 1, 'e': 6, 's': 2, 't': 4, 'é': 1, '.': 2, 'v': 1, 'a': 1}
# ```
# 
# **Observação**: Mais adiante no curso, aprenderemos a lidar com a pontuação.

# %%
# solução


def analisar_texto(texto):
    
    palavras = texto.split()  # separa com base em espaços
    contagem_palavras = len(palavras)
    frequencia_palavras = {}
    frequencia_letras = {}
    
    for palavra in palavras:
        # abaixo, o get verificará se existe a palavra no dicionário. Não havendo, atribui o valor 0 e soma 1
        frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1
        for letra in palavra.lower():
            # abaixo, o get verificará se existe a letra no dicionário. Não havendo, atribui o valor 0 e soma 1
            frequencia_letras[letra] = frequencia_letras.get(letra, 0) + 1
            
    return contagem_palavras, frequencia_palavras, frequencia_letras


texto = "Olá mundo! Este é um teste. Olá novamente."
contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)
print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequência de palavras: {frequencia_palavras}")
print(f"Frequência de letras: {frequencia_letras}")




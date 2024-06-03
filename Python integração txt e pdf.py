
# 
# ### Para os nossos exemplos, vamos avaliar o Release de Resultados do 3º e 4º Trimestre de 2020 da Magazine Luiza

# %% [markdown]
# #### 1º Objetivo: Queremos conseguir separar apenas o DRE do Release de Resultados (Página 14) para enviar para a Diretoria, como fazemos?
#     - Separar as páginas de um pdf

# %%
import PyPDF2 as pyf
from pathlib import Path

nome = 'MGLU_ER_3T20_POR.pdf'
arquivo_pdf = pyf.PdfReader(nome) # Abrir PDF

# Vai percorrer cada paginado pdf

for i,pagina in enumerate(arquivo_pdf.pages):     # Ele transforma cada pagina do pdf em um item,ou seja, forma uma lista.
    num_pagina = i + 1
    novo_pdf = pyf.PdfWriter() # Está criando um novo arquivo
    novo_pdf.add_page(pagina) # Adicionar a pagina dentro do arquivo
    with Path(f'paginas/Arquivo pagina {num_pagina}.pdf').open(mode='wb') as arquivo:
        novo_pdf.write(arquivo) # Vai rodar dentro with para salvar as informações


# %% [markdown]
# #### 2º Objetivo: Com o Release de Resultados já separado página por página, queremos incluir apenas as Páginas de Destaque (Página 1), DRE (Página 14) e Balanço (Página 16).
#     - Juntar vários pdfs em 1

# %%
num_paginas = [1, 14, 16]
novo_arquivo = pyf.PdfWriter() # Está criando um novo arquivo, passando paginas do arquivo
for num in num_paginas:
    pagina_pdf = pyf.PdfReader(f'paginas/Arquivo pagina {num}.pdf')
    novo_arquivo.add_page(pagina_pdf.pages[0]) 
    with Path('Consolidado.pdf').open(mode='wb') as arquivo:
        novo_arquivo.write(arquivo)


# %% [markdown]
# ### Extra: Para adicionar todas as páginas de 2 pdfs

# %%
pdf_mesclado = pyf.PdfMerger()
pdf_mesclado.append('MGLU_ER_3T20_POR.pdf')
pdf_mesclado.append('MGLU_ER_4T20_POR.pdf')

with Path('Arquivo_mesclado.pdf').open(mode='wb') as arquivo: # O 'w' serve para escrever no arquivo e o 'b' é por que é um arquivo pdf
    pdf_mesclado.write(arquivo)


# %% [markdown]
# # Funcionalidades que podem ser úteis:
# 
# - Inserir arquivo no meio do outro
# - Quero colocar dentro do Resultado do 4T20 os destaques do 3T20 para poder comparar os 2 dentro do mesmo relatório

# %%
pdf_mesclado2 = pyf.PdfMerger() #Passa o arquivvo completo
pdf_mesclado2.append('MGLU_ER_4T20_POR.pdf')
pdf_mesclado2.merge(1, 'paginas/Arquivo pagina 1.pdf') #O primeiro parâmetro vai ser a posição que voce quer adicionar, e o segundo parâmetro vai ser o arquivo

with Path('relatorio.pdf').open(mode='wb') as arquivo:
    pdf_mesclado2.write(arquivo)

# %% [markdown]
# - Rodar Página

# %%
arquivo_pdf_og = pyf.PdfReader('MGLU_ER_3T20_POR.pdf')
novo_arquivo = pyf.PdfWriter()

for pagina in arquivo_pdf_og.pages:
    pagina.rotate(90)
    novo_arquivo.add_page(pagina)

with Path('arquivo rotacionado.pdf').open(mode='wb') as arquivo:
    novo_arquivo.write(arquivo)

# %% [markdown]
# # Trabalhando com Textos e Informações Dentro do PDF
# 
# #### 1º Objetivo: Quero identificar como foram as Despesas com Vendas da MGLU
#     - Pegar texto da página e identificar onde está essa informação

# %%
arquivo = pyf.PdfReader('MGLU_ER_3T20_POR.pdf')  # Ler o pdf

qtd_paginas = len(arquivo.pages)
print(qtd_paginas)

metadados_arquivo = arquivo.metadata  # Informações do arquivo
print(metadados_arquivo)

texto_referencia = '| Despesas com Vendas'  # procurar uma referencia para extrair o texto que você quer

for i,pagina in enumerate(arquivo.pages):
    texto_pagina = pagina.extract_text()      # função para extrair/procurar pedaços de texto
    if texto_referencia in texto_pagina:
        print(f'Numero pagina:{i + 1}')
        texto_analisar = texto_pagina        # Atribuindo o texto a uma variavel 

# %%

posiçao_inicial = texto_analisar.find(texto_referencia)
posiçao_final = texto_analisar.find('| Despesas Gerais e Administrativas')
texto_final = texto_analisar[posiçao_inicial : posiçao_final]
print(texto_final)

# %% [markdown]
# #### 2º Objetivo: Quero analisar o DRE (sem ajuste - Página 5)
#     - Para ler tabelas em pdf, use o tabula (é ninja)
#     
#     - Cuidado 1: Instale o tabula-py (não instale o tabula). Se instalar o tabula errado, desinstale ele, instale o tabula-py, desinstale o tabula-py e instale novamente o tabula-py. Reinicie o kernel do Jupyter após isso
#     
#     - Cuidado 2: Tem que ter o java instalado no seu computador (depois de instalar, reinicie o computador)

# %%
import tabula

tabelas = tabula.read_pdf('MGLU_ER_3T20_POR.pdf', pages=5) # Vai retornar uma lista de tabelas
df_resultado = tabelas[0]
# Excluir linhas totalmentes vazias
df_resultado = df_resultado.dropna(how='all',axis=0)  # Vai retirar todos os valores vazios,como axis é igual a 0,então é linhas

# Excluir colunas totalmentes vazias
df_resultado = df_resultado.dropna(how='all',axis=1)
# display(df_resultado)

# Tornando a linha no cabecario do dataframe
df_resultado.columns = df_resultado.iloc[0]
df_resultado = df_resultado[1:]

# Retirando os indices errados
df_resultado = df_resultado.reset_index(drop=True) # O drop=True(se não colocar os indices vao virar coluna)* Testar com e sem o true para ver a diferença
display(df_resultado)

# %% [markdown]
# #### 3º Objetivo: Quero analisar o Capital de Giro e os Investimentos (ambas as tabelas na página 12)
#     - Páginas com mais de 1 tabela

# %%
tabelas = tabula.read_pdf('MGLU_ER_3T20_POR.pdf',pages=12) # é a página original do pdf,ou seja, o indice da pagina no pdf
for tabela in tabelas:
    tabela = tabela.dropna(how='all',axis=0) # Retirando linhas vazias
    tabela = tabela.dropna(how='all',axis=1) # Retirando colunas vazias
    tabela = tabela.reset_index(drop=True) # Ordenanddo de maneira correta os índices
    display(tabela)

# %% [markdown]
# #### O que fazer quando o tabula não consegue ler alguma linha da tabela? Como o cabeçalho, no nosso caso?

# %%
df_capital_giro = tabelas[0]
df_capital_giro = df_capital_giro.dropna(how='all',axis=0)
df_capital_giro = df_capital_giro.reset_index(drop=True)
display(df_capital_giro) # Número entre parenteses é pq são negativos

tabelas2 = tabula.read_pdf('MGLU_ER_3T20_POR.pdf',pages=12, lattice=True) # O lattice vai ler o dataframe de outra maneira
df_capital_giro2 = tabelas2[0]
df_capital_giro2 = df_capital_giro2.dropna(how='all',axis=0)
df_capital_giro2 = df_capital_giro2.dropna(how='all',axis=1)
df_capital_giro2 = df_capital_giro2.reset_index(drop=True)
colunas = df_capital_giro2.iloc[0]
colunas = colunas.dropna() # Retirou os valores vazios
df_capital_giro.columns = colunas # Ta atribuindo as colunas do dt2 para o dataframe original
display(df_capital_giro)



# %% [markdown]
# # Outro método que pode ser útil algum dia: Captar Imagem em um pdf
#     - biblioteca pikepdf

# %%
from pikepdf import Pdf,PdfImage

arquivo = Pdf.open('MGLU_ER_3T20_POR.pdf')

for pagina in arquivo.pages:
    for nome, imagem in pagina.images.items(): # Vai pegar todos os itens da imagem da pagina,ou seja, pegar todas as imagens
        imagem_salvar = PdfImage(imagem)
        imagem_salvar.extract_to(fileprefix=f'imagens/{nome}') #Nome do arquivo,no caso vai ser a variável nome
    # Realizando um upacking da tupla




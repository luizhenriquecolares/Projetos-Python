
# - Usar o https://web.whatsapp.com/send?phone=numero&text=texto (mais fácil, mais seguro, mas mais demorado)
# 

# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")

# esperar a tela do whatsapp carregar
while len(navegador.find_elements(By.ID, 'side')) < 1: # -> lista for vazia -> que o elemento não existe ainda
    # esse find é uma tela que so aparece quando o zap está aberto
    time.sleep(1)
time.sleep(2) # só uma garantia

# %%
# o whatsapp já carregou
import pandas as pd

tabela = pd.read_excel("Envios.xlsx")
display(tabela[['nome', 'mensagem', 'arquivo']]) # tem também uma coluna telefone dentro da tabela

# %%
import urllib
import time
import os

for linha in tabela.index:
    # enviar uma mensagem para a pessoa
    nome = tabela.loc[linha, "nome"]
    mensagem = tabela.loc[linha, "mensagem"]
    arquivo = tabela.loc[linha, "arquivo"]
    telefone = tabela.loc[linha, "telefone"]
    
    texto = mensagem.replace("fulano", nome)
    texto = urllib.parse.quote(texto)

    # enviar a mensagem
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}" # Esse link faz com que leve diretamente para uma conversa e enviando uma msg
    
    navegador.get(link)
    # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
    while len(navegador.find_elements(By.ID, 'side')) < 1: # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(1)
    time.sleep(2) # só uma garantia
    
    # você tem que verificar se o número é inválido
    if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
        # Verificando se o texto de número inválido não aparece na tela,ou seja,menor que 1 (< 1)
        # enviar a mensagem
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        
        if arquivo != "N":
            caminho_completo = os.path.abspath(f"arquivos/{arquivo}")
            navegador.find_element(By.XPATH, 
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
            navegador.find_element(By.XPATH, 
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(caminho_completo)
            # Está preenchendo o XPATH do input do arquivo,com isso falta só pegar o XPATH do botão de enviar
            time.sleep(2)
            navegador.find_element(By.XPATH, 
                                   '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
            # XPATH do botão de enviar
            
        time.sleep(5)



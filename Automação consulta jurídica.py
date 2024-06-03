# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# %%
import os

caminho = os.getcwd()
arquivo = caminho + r"\index.html"
navegador.get(arquivo)

# %%
import pandas as pd
tabela = pd.read_excel('Processos.xlsx')
display(tabela)

# %%
from selenium.webdriver import ActionChains
import time
time.sleep(2)

for linha in tabela.index:

    navegador.get(arquivo)

    # Abrir lista de cidades
    botao = navegador.find_element(By.CLASS_NAME,'dropdown-menu')
    ActionChains(navegador).move_to_element(botao).perform()

    # Selecionando a cidade:

    cidade = tabela.loc[linha,'Cidade']
    navegador.find_element(By.PARTIAL_LINK_TEXT,cidade).click()

    # Mudar para nova aba

    aba_original = navegador.window_handles[0]
    indice = 1 + linha
    nova_aba = navegador.window_handles[indice]

    # Mudando o navegaodr para a nova aba
    navegador.switch_to.window(nova_aba)

    # Preenchendo

    navegador.find_element(By.ID,'nome').send_keys(tabela.loc[linha,"Nome"])
    navegador.find_element(By.ID,'advogado').send_keys(tabela.loc[linha,"Advogado"])
    navegador.find_element(By.ID,'numero').send_keys(tabela.loc[linha,"Processo"])

    # Clicar no botão
    navegador.find_element(By.CLASS_NAME,'registerbtn').click()

    # confirmar pesquisa
    alerta = navegador.switch_to.alert # Salvando o alerta
    alerta.accept()

    # Esperar o resultado da pesquisa e agir de acordo com o resultado
    
    import time
    while True:
        try:
            alerta_texto = navegador.switch_to.alert
            break
        except:
            time.sleep(1)

    texto_alerta = alerta_texto.text

    if 'Processo encontrado com sucesso' in texto_alerta:
        alerta_texto.accept()
        tabela.loc[linha,"Status"] = 'Encontrado'
    else:
        tabela.loc[linha,"Status"] = 'Não Encontrado'
        alerta.accept()


# %%
display(tabela)



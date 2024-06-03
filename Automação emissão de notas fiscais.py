# %%
# entrar na página de login

# preencher login e senha

# clicar no botão de fazer login

# preencher os dados da nf

# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\jacia\OneDrive\Área de Trabalho\Projeto automação",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico,options=options)
# Se o site estivesse no chrome e não nos arquivos,deveria colocar navegador.get('https......')
navegador.get(r'C:\Users\jacia\OneDrive\Área de Trabalho\Projeto automação\login.html')


# %%
# preencher login e senha
navegador.find_element(By.XPATH,'/html/body/div/form/input[1]').send_keys('Lcolares91@gmail.com')
navegador.find_element(By.XPATH,'/html/body/div/form/input[2]').send_keys('luiz123')
# clicar no botão para finalizar cadastro
navegador.find_element(By.XPATH,'/html/body/div/form/button').click()


# %%
# preencher os dados da nf
# Importar base de dados
import pandas as pd

tabela = pd.read_excel("NotasEmitir.xlsx") 
display(tabela)


# %%
# preencher os dados da nf
for linha in tabela.index: # Vai percorrer as linhas
    navegador.find_element(By.NAME, 'nome').send_keys(tabela.loc[linha, "Cliente"]) # nome

    navegador.find_element(By.NAME,'endereco').send_keys(tabela.loc[linha, "Endereço"]) # endereco

    navegador.find_element(By.NAME,'bairro').send_keys(tabela.loc[linha, 'Bairro']) # bairro

    navegador.find_element(By.NAME,'municipio').send_keys(tabela.loc[linha, 'Municipio']) # municipio

    navegador.find_element(By.NAME,'cep').send_keys(str(tabela.loc[linha, 'CEP'])) # cep

    # navegador.find_element(By.XPATH,'//*[@id="formulario"]/select/option[11]').click()
    navegador.find_element(By.NAME,'uf').send_keys(tabela.loc[linha, 'UF'])

    navegador.find_element(By.NAME,'cnpj').send_keys(str(tabela.loc[linha, 'CPF/CNPJ'])) # cnpj

    navegador.find_element(By.NAME,'inscricao').send_keys(str(tabela.loc[linha,'Inscricao Estadual'])) # inscricao

    navegador.find_element(By.NAME,'descricao').send_keys(tabela.loc[linha,'Descrição']) # descricao

    navegador.find_element(By.NAME,'quantidade').send_keys(str(tabela.loc[linha,'Quantidade'])) # quantidade

    navegador.find_element(By.NAME,'valor_unitario').send_keys(str(tabela.loc[linha,'Valor Unitario'])) # valor_unitario

    navegador.find_element(By.NAME,'total').send_keys(str(tabela.loc[linha,'Valor Total'])) # total

    # Clicar em emitir nota fiscal

    navegador.find_element(By.XPATH,'//*[@id="formulario"]/button').click()

    # Recarregar a pagina para limpar o formulário
    navegador.refresh()

navegador.quit()




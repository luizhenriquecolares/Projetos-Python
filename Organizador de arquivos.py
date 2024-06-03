import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta") # esse camino é onde esta a pasta 

lista_arquivos = os.listdir(caminho)
# Arquivos que estao na pasta selecionada

locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "Musica" : [".mp3"]
}

for arquivo in lista_arquivos:
    # 01. ARquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
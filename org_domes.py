import PyPDF2
import re
import os
import shutil
from datetime import datetime
import locale


path = "C:/Users/Usuario/Desktop/EMPRESAS/TESTES/"
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
caminho = f"C:/Users/Usuario/Desktop/EMPRESAS/Domestica/"

nomes_zuas = {
    'FRANCISCO BENEDITO CARVALHO PERESTRELO': 'FRANCISCO BENEDITO CARVALHO PERESTRELO',
    'TELMAMARIAGARCIA BAZZETTI': 'TELMA MARIA GARCIA BAZZETTI',
    'WALDOMIRO DASILVAFERREIRA': 'WALDOMIRO DA SILVA FERREIRA',
    'ELIOPECINES': 'ELIO PECINES',
    'FERNANDA SANCHES SABION GUIRADO': 'FERNANDA SANCHES SABION GUIRADO',
    'SAMIACAVALIERI ABOUASSILORENZI': 'SAMIA CAVALIERI ABOU ASSI LORENZI',
    'AURORA ROSALEILA': 'AURORA ROSA LEILA',
    'EUNICE APARECIDA RODRIGUES GUIRADO': 'EUNICE APARECIDA RODRIGUES GUIRADO',
    'DULCINERIA GARCIA LOPESBASSAN': 'DULCINERIA GARCIA LOPES BASSAN',
    'BRUNA LETICIA PEREIRA DASILVA': 'BRUNA LETICIA PEREIRA DA SILVA',
    'ABDELMAJIDSADAHMAD LEILA': 'ABDEL MAJID SAD AHMAD LEILA',
    'LUCYMARYDESANTANNA': 'LUCY MARY DE SANTANNA',
    'MARIAVILMADEMELOBALDAN': 'MARIA VILMA DE MELO BALDAN'}

arqs = []
for i in os.listdir():
    if '.pdf' in i:
        arqs.append(i)


for file in arqs:
    pdf_file = open(f"{path}{file}", 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)
    page = read_pdf.pages[0]
    page_co = page.extract_text()
    my = page_co.split('\n')

    #local_name = my[4].index('CPF:')
    #print(my[4][:local_name])
    # print(my[2].index("Nome:"))
    print(my[0][38:])
    #print(my[0][:36])
    #print(my[2][20:].replace("Nome:", ""))
    if my[0] == 'VIA DO EMPREGADO':
        local_name = my[4].index('CPF:')
        pasta_nome = my[4][:local_name].strip().split(" ")
        pasta_nome = '_'.join(pasta_nome).replace("&", "E")
        print(pasta_nome)

        data = my[1].replace("Competência", "").strip()
        pdf_file.close()
        date_num = datetime.strptime(data, "%B/%Y")
        date_num = date_num.strftime("%m/%Y")
        mes, ano = date_num.split('/')
        print(f"{mes} ---- {ano}")

        arquivo_name = f"{pasta_nome}_Demonstrativo_Recibo-{mes}-{ano}.pdf"
        os.rename(str(path+file), str(path+arquivo_name))
        caminho_final = str(caminho+pasta_nome+'/'+ano+'/'+mes)

        try:
            if os.path.isdir(caminho_final):
                shutil.move(path+arquivo_name, caminho_final)
                print(f"Arquivo Movido: {pasta_nome}")
            else:
                os.makedirs(caminho_final)
                shutil.move(path+arquivo_name, caminho_final)
                print(f"Pasta criada e Arquivo Movido: {pasta_nome}")

        except (FileNotFoundError, FileExistsError, shutil.Error):
            print(f"Ocorreu um erro ao mover o arquivo: {pasta_nome}\n")

    elif my[0][:36] == 'Relatório Consolidado deRemunerações':
        nome = my[2][20:].replace("Nome:", "")
        print(nome)
        for names in nomes_zuas:
            if names == nome:
                nome_pasta = nomes_zuas[names]
                nome_pasta = nome_pasta.strip().split(" ")
                nome_pasta = '_'.join(nome_pasta)
        
        data = my[0][38:].strip()
        date_num = datetime.strptime(data, "%B/%Y")
        date_num = date_num.strftime("%m/%Y")
        mes, ano = date_num.split('/')
        pdf_file.close()

        arquivo_name = f"{nome_pasta}_Relatorio_Consolidado-{mes}-{ano}.pdf"
        os.rename(str(path+file), str(path+arquivo_name))
        caminho_final = str(caminho+nome_pasta+'/'+ano+'/'+mes)

        try:
            if os.path.isdir(caminho_final):
                shutil.move(path+arquivo_name, caminho_final)
                print(f"Arquivo Movido: {nome_pasta}\n")
            else:
                os.makedirs(caminho_final)
                shutil.move(path+arquivo_name, caminho_final)
                print(f"Pasta Criada Arquivo Movido: {nome_pasta}\n")
        except shutil.Error:
            print(f"Ocorreu um erro ao mover o arquivo: {nome_pasta}\n")

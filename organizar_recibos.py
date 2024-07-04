import PyPDF2
import re
import os
import tabula
import shutil

# Recibo_52435161000101_032023_40_0000050000124265642.pdf
#pdf_file = open('C:/Users/Usuario/Desktop/EMPRESAS/Recibo_52435161000101_032023_40_0000050000124265642.pdf', 'rb')
#read_pdf = PyPDF2.PdfReader(pdf_file)

#page = read_pdf.pages[0]
#page_co = page.extract_text()
path = "C:/Users/Usuario/Desktop/EMPRESAS/TESTES/"

caminho1 = f"C:/Users/Usuario/Desktop/EMPRESAS/Com Funcionario/"
caminho2 = f"C:/Users/Usuario/Desktop/EMPRESAS/Sem Funcionario/"
caminho3 = f"C:/Users/Usuario/Desktop/EMPRESAS/Sem Movimento/"
caminho4 = f"C:/Users/Usuario/Desktop/EMPRESAS/Sem Movimento/"

arq = []
for i in os.listdir():
    if '.pdf' in i:
        arq.append(i)


for file in arq:
    pdf_file = open(f'C:/Users/Usuario/Desktop/EMPRESAS/TESTES/{file}', 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)
    page = read_pdf.pages[0]
    page_co = page.extract_text()
    my = page_co.split('\n')

    if "Nome" in my[5]:
        nome = my[5].replace("Nome ", "").strip().split(" ")
    else:
        nome = my[4].replace("Nome", "").strip().split(" ")

    pasta_nome = '_'.join(nome).replace("&", "E")

    # Os recibos do Newton da advogacia vem com um nome na guia e outro abreviado no recibo
    if pasta_nome == 'NEWTON_CARLOS_DE_SOUZA_BAZZETTI_SOCIEDADE_DE':
        pasta_nome += '_ADVOG'

    # O nome da pasta da Clinica esta com LT abreviado na pasta
    elif pasta_nome == 'CLINICA_DE_MEDICINA_DE_TRAFEGO_SABION_E_GUIRADO_LTDA':
        pasta_nome = pasta_nome.replace('LTDA', 'LT')

    elif pasta_nome == "36.301.432_REGIANE_SIMPLICIO_DA_SILVA_ANDRADE":
        pasta_nome = pasta_nome.replace("36.301.432_", "")

    elif pasta_nome == "TECNO_-_CAIXAS_INDUSTRIA_E_COMERCIO_DE_EMBALAGENS_LTDA":
        pasta_nome = pasta_nome.replace("_LTDA", "")
        
    for i in my:
        
        if "Período de apuração " in i:
            if '2023' == i.replace("Período de apuração ", ""):
                ano = '2023'
                mes = '13'
            else:
                mes, ano = i.replace("Período de apuração ", "").split('/')
    

    ano = ano.strip()
    arquivo_nome = 'Recibo_'+pasta_nome+'-'+mes+'-'+ano+'.pdf'
    #print(str(caminho1+pasta_nome+'/'+ano))
    print(pasta_nome)
    pdf_file.close()

    if os.path.isdir(str(caminho1+pasta_nome)):
        
        if os.path.isfile(str(caminho1+pasta_nome+'/'+ano+'/'+mes+'/'+arquivo_nome)):
            #os.makedirs()
            arquivo_nome = 'Recibo_'+pasta_nome+'-'+mes+'-'+ano+'-retificado'+'.pdf'
            
            try:
                os.makedirs(str(caminho1+pasta_nome+'/'+ano+'/'+mes))
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho1+pasta_nome+'/'+ano+'/'+mes))
            except FileExistsError:
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho1+pasta_nome+'/'+ano+'/'+mes))
        
        else:
            try:
                os.makedirs(str(caminho1+pasta_nome+'/'+ano+'/'+mes))
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho1+pasta_nome+'/'+ano+'/'+mes))
            except FileExistsError:
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho1+pasta_nome+'/'+ano+'/'+mes))
    
    elif os.path.isdir(str(caminho2+pasta_nome)):
        if os.path.isfile(str(caminho2+pasta_nome+'/'+ano+'/'+mes+'/'+arquivo_nome)):
            #os.makedirs()
            arquivo_nome = 'Recibo_'+pasta_nome+'-'+mes+'-'+ano+'-retificado'+'.pdf'
            
            try:
                os.makedirs(str(caminho2+pasta_nome+'/'+ano+'/'+mes))
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho2+pasta_nome+'/'+ano+'/'+mes))
            except FileExistsError:
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho2+pasta_nome+'/'+ano+'/'+mes))
        
        else:
            try:
                os.makedirs(str(caminho2+pasta_nome+'/'+ano+'/'+mes))
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho2+pasta_nome+'/'+ano+'/'+mes))
            except FileExistsError:
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho2+pasta_nome+'/'+ano+'/'+mes))

    elif os.path.isdir(str(caminho3+pasta_nome)):
        if os.path.isfile(str(caminho3+pasta_nome+'/'+ano+'/'+mes+'/'+arquivo_nome)):
            #os.makedirs()
            arquivo_nome = 'Recibo_'+pasta_nome+'-'+mes+'-'+ano+'-retificado'+'.pdf'
            
            try:
                os.makedirs(str(caminho3+pasta_nome+'/'+ano+'/'+mes))
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho3+pasta_nome+'/'+ano+'/'+mes))
            except FileExistsError:
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho3+pasta_nome+'/'+ano+'/'+mes))
        
        else:
            try:
                os.makedirs(str(caminho3+pasta_nome+'/'+ano+'/'+mes))
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho3+pasta_nome+'/'+ano+'/'+mes))
            except FileExistsError:
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho3+pasta_nome+'/'+ano+'/'+mes))

    elif os.path.isdir(str(caminho4+pasta_nome)):
        if os.path.isfile(str(caminho4+pasta_nome+'/'+ano+'/'+mes+'/'+arquivo_nome)):
            #os.makedirs()
            arquivo_nome = 'Recibo_'+pasta_nome+'-'+mes+'-'+ano+'-retificado'+'.pdf'
            
            try:
                os.makedirs(str(caminho4+pasta_nome+'/'+ano+'/'+mes))
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho4+pasta_nome+'/'+ano+'/'+mes))
            except FileExistsError:
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho4+pasta_nome+'/'+ano+'/'+mes))
        
        else:
            try:
                os.makedirs(str(caminho4+pasta_nome+'/'+ano+'/'+mes))
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho4+pasta_nome+'/'+ano+'/'+mes))
            except FileExistsError:
                os.rename(file, arquivo_nome)
                shutil.move(str(path+arquivo_nome), str(caminho4+pasta_nome+'/'+ano+'/'+mes))

    else:
        print("Pasta não econtrada!")    

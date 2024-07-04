import os
import tabula
import shutil
import PyPDF2
from datetime import datetime
import locale


def substituir_vazio(item):
    return item if item != '' else 'E'


locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

arqvs = []
for i in os.listdir():

    if '.PDF' in i or '.pdf' in i:
        arqvs.append(i)

nomes_guias = []
for file in arqvs:

    pdf_file = open(f"C:/Users/Usuario/Desktop/EMPRESAS/TESTES/{file}", "rb")
    read_pdf = PyPDF2.PdfReader(pdf_file)
    page = read_pdf.pages[0]
    page_co = page.extract_text()
    my = page_co.split('\n')
    print(my)
    
    if my[1] == "de Receitas Federais":

        if my[3][:14] == "018.888.598-65":
            path = my[3][15:].split(" ")
        else:
            path = my[3][19:].split(" ")
        pasta_name = "_".join(path).replace("&", "E")


        if my[8] == "13º salárioValor Total do Documento":
            data_comp = my[14].replace("PA:", "").replace("Vencimento:", "").split(" ")
        else:
            data_comp = my[13].replace("PA:", "").replace("Vencimento:", "").split(" ")


        if data_comp[1] == my[6].replace("Observações", ""):

            new_name = "Guia"+"_"+pasta_name+"-"+data_comp[0].replace("/", "-")
            nomes_guias.append((file, new_name, data_comp[0], pasta_name))
            pdf_file.close()

        else:

            new_name = "Guia_"+pasta_name+"-"+data_comp[0].replace("/", "-")+"-Recalculado"
            nomes_guias.append((file, new_name, data_comp[0], pasta_name))
            pdf_file.close()

    elif my[1] == "do eSocial":

        if my[2] == '36.301.432/0001-80 36.301.432 REGIANE SIMPLICIO DA SILVA ANDRADE':

            path = my[2][19:].split(" ")
            path = path[1:]
            vencimento_var = my[7][:10]
        
        elif my[8] == '13º salário Valor Total do Documento':

            path = my[2][15:].split(" ")
            vencimento_var = my[-3].replace("Pagar até: ", "")

        else:
            # print(my[26])
            path = my[2][15:].split(" ")
            vencimento_var = my[30].replace("Pagar até: ", "")
        
        pasta_name = "_".join(path).replace("&", "E")
        
        data_comp = my[4].replace('Data de Vencimento', '')
        
        if data_comp == '2023':
            mes = '13'
            ano = '2023'
            date_num = f"{mes}/{ano}"
        else:
            date_num = datetime.strptime(data_comp, "%B/%Y")
            date_num = date_num.strftime("%m/%Y")
            mes, ano = date_num.split('/')


        if my[5].replace("Número do Documento", "") == vencimento_var:

            new_name = "Guia"+"_"+pasta_name+"-"+mes
            nomes_guias.append((file, new_name, date_num, pasta_name))
            pdf_file.close()

        else:

            new_name = "Guia_"+pasta_name+"-"+mes+"-Recalculado"
            nomes_guias.append((file, new_name, date_num, pasta_name))
            pdf_file.close()

    elif my[10] == " GFD - Guia do FGTS Digital":

        if 'MENSAL' in my[6]:

            path = my[2].split(" ")
            path = list(filter(lambda x: x != '', map(substituir_vazio, path)))
            #print(path)
            pasta_name = "_".join(path).replace("&", "E")

            data_comp = my[6][9:16].replace("/", "-")
            
            if pasta_name == "CLINICA_DE_MEDICINA_DE_TRAFEGO_SABION_E_GUIRADO_LTD":
                pasta_name = "CLINICA_DE_MEDICINA_DE_TRAFEGO_SABION_E_GUIRADO_LT"

            new_name = "Guia_FGTS_"+pasta_name+"-"+data_comp
            nomes_guias.append((file, new_name, my[6][9:16], pasta_name))

            pdf_file.close()
        
        else:

            pdf_file.close()


for i in nomes_guias:

    novo_arq_name = str(i[1]+".pdf")

    if i[2] == '2023':
        mes = '13'
        ano = '2023'
    else:
        mes, ano = i[2].split("/")
    local = "C:/Users/Usuario/Desktop/EMPRESAS/TESTES/"
    os.rename(str(local+i[0]), str(local+novo_arq_name))

    caminho1 = f"C:/Users/Usuario/Desktop/EMPRESAS/Com Funcionario/{i[3]}"
    caminho2 = f"C:/Users/Usuario/Desktop/EMPRESAS/Sem Funcionario/{i[3]}"
    caminho3 = f"C:/Users/Usuario/Desktop/EMPRESAS/Domestica/{i[3]}"
                
    try:

        if os.path.isdir(caminho1):

            if os.path.isdir(str(caminho1+"/"+ano+"/"+mes)):

                shutil.move(str(local+novo_arq_name), str(caminho1+"/"+ano+"/"+mes))
                print("Com funcionario")
                
            else:

                os.makedirs(str(caminho1+"/"+ano+"/"+mes))
                print(f"Pasta criada - Com Funcionario: {mes}")
                shutil.move(str(local+novo_arq_name), str(caminho1+"/"+ano+"/"+mes))
                
        elif os.path.isdir(caminho2):

            if os.path.isdir(str(caminho2+"/"+ano+"/"+mes)):

                print("Sem funcionario")
                shutil.move(str(local+novo_arq_name), str(caminho2+"/"+ano+"/"+mes))

            else:

                os.makedirs(str(caminho2+"/"+ano+"/"+mes))
                print(f"Pasta criada - Sem funcionario: {mes}")
                shutil.move(str(local+novo_arq_name), str(caminho2+"/"+ano+"/"+mes))
        
        elif os.path.isdir(str(caminho3)):

            if os.path.isdir(str(caminho3+"/"+ano+"/"+mes)):
                shutil.move(str(local+novo_arq_name), str(caminho3+"/"+ano+"/"+mes))

            else:

                os.makedirs(str(caminho3+"/"+ano+"/"+mes))
                print("Pasta Criada - Domestica")
                shutil.move(str(local+novo_arq_name), str(caminho3+"/"+ano+"/"+mes))
                
        else:

            print("Não encontrado")
            print(i[3])

    except:

        print("Algo deu errado")


"""Para Imprimir o nome no Recibo"""
# print(my[5])

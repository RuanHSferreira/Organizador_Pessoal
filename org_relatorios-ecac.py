import os
import shutil
import PyPDF2


arqvs = []
for i in os.listdir():
    if '.pdf' in i:
        arqvs.append(i)

    
nomes = []
for file in arqvs:

    pdf_file = open(f'C:/Users/Usuario/Desktop/EMPRESAS/TESTES/{file}', 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)
    page = read_pdf.pages[0]
    page_co = page.extract_text()
    my = page_co.split("\n")

    # data emissão my[2]
    # nome my[4]

    data = my[2].replace("PROCURADORIA-GERAL DA FAZENDA NACIONAL ", "")[:-3]
    ano = data.split('/')[2][:4]
    mes = data.split('/')[1]
    data = data.replace('/', '_').replace(' ', '_hora_'). replace(':', '-')
    empre_nome = my[4][19:]
    empre_nome = '_'.join(empre_nome.split(' ')).replace("&", "E")
    # empre_nome.split()

    nome_guia = f"Relatorio_{empre_nome}_{data}.pdf"

    nomes.append((file, empre_nome, nome_guia, data, ano, mes))
    pdf_file.close()


for file in nomes:

    local = "C:/Users/Usuario/Desktop/EMPRESAS/TESTES/"
    os.rename(str(local+file[0]), str(local+file[2]))

    caminho1 = f"C:/Users/Usuario/Desktop/EMPRESAS/Com Funcionario/{file[1]}"
    caminho2 = f"C:/Users/Usuario/Desktop/EMPRESAS/Sem Funcionario/{file[1]}"
    caminho3 = f"C:/Users/Usuario/Desktop/EMPRESAS/Domestica/{file[1]}"
    caminho4 = f"C:/Users/Usuario/Desktop/EMPRESAS/Sem Movimento/{file[1]}"

    ano = file[4]
    mes = file[5]
   
    try:

        if os.path.isdir(caminho1):

            if os.path.isdir(str(caminho1+"/"+ano+"/"+mes)):

                shutil.move(str(local+file[2]), str(caminho1+"/"+ano+"/"+mes))
                print("Com funcionario")
                
            else:

                os.makedirs(str(caminho1+"/"+ano+"/"+mes))
                print(f"Pasta criada - Com Funcionario: {mes}")
                shutil.move(str(local+file[2]), str(caminho1+"/"+ano+"/"+mes))
                
        elif os.path.isdir(caminho2):

            if os.path.isdir(str(caminho2+"/"+ano+"/"+"RELATORIOS")):

                print("Sem funcionario")
                shutil.move(str(local+file[2]), str(caminho2+"/"+ano+"/"+"RELATORIOS"))

            else:

                os.makedirs(str(caminho2+"/"+ano+"/"+'RELATORIOS'))
                print(f"Pasta criada - Sem funcionario: ")
                shutil.move(str(local+file[2]), str(caminho2+"/"+ano+"/"+"RELATORIOS"))
        
        elif os.path.isdir(str(caminho3)):

            if os.path.isdir(str(caminho3+"/"+ano+"/"+mes)):
                shutil.move(str(local+file[2]), str(caminho3+"/"+ano+"/"+mes))

            else:

                os.makedirs(str(caminho3+"/"+ano+"/"+mes))
                print("Pasta Criada - Domestica")
                shutil.move(str(local+file[2]), str(caminho3+"/"+ano+"/"+mes))
                
        elif os.path.isdir(str(caminho4)):

            if os.path.isdir(str(caminho4+"/"+ano+"/"+mes)):
                shutil.move(str(local+file[2]), str(caminho4+"/"+ano+"/"+mes))

            else:

                os.makedirs(str(caminho4+"/"+ano+"/"+mes))
                print("Pasta Criada - Sem Movimento")
                shutil.move(str(local+file[2]), str(caminho4+"/"+ano+"/"+mes))
            
        else:

            print("Não encontrado")
            print(file[1])

    except:

        print("Algo deu errado")

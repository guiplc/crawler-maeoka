#VER COMPARACAO DE PRODUTO NO SITE DA FAST SHOP

import requests
import time
from bs4 import BeautifulSoup

#Crawler FASTSHOP
start=time.time()
def FastShop(max_produtos): #vasculhando a página de catálogo dos produtos
    arquivo_descrip = open('Dados', 'w') #preciso ter essa variável que é para abrir o arquivo?
    arquivo_titulos = open('Titulos', 'w')
    arquivo_HTML=open('TotalHTML','w') #preciso ter essa variável que é para abrir o arquivo?
    arquivo_linksTotal = open ('LinksProdutos','w')
    arquivo_Erros = open ('LogErros','w')
    listaDepart=set(open('Departamentos2.txt').read().split())
    qntProdutos=0
    for url in listaDepart:
        produtos=1
        source_code = requests.get(url) #guarda todas as informações do HTML daquela página
        plain_text = source_code.text #transforma toda as informações em texto
        soup = BeautifulSoup(plain_text, "lxml") #convertendo o conteúdo em um BeautifulSoup object e armazenando ele no soup
        spanProd=soup.find('span',{'class':'num_products'}).get_text()
        spanProd=" ".join(spanProd.split())
        spanProd=spanProd.split('de')
        spanProd=spanProd[1].split()
        spanProd=int(spanProd[0])
        print ('Departamento: ',url,'\nNúmero de Produtos:',spanProd,'\n')
        qntProdutos=qntProdutos+spanProd
        contadorProdDepart=1
#        with open ('Dados','a') as file:
#            file.write('ENTROU MAINNN')
#        while produtos<=max_produtos: #varre as páginas
        for link in soup.find_all('a', {'class': 'prod-image-area'}):
            if produtos>max_produtos:
                break
            if contadorProdDepart>spanProd:
                break
            href = link.get('href')
            with open ('LinksProdutos','a') as file:
                file.write(href+'\n')
            try:
                get_title(href,produtos)
            except:
                print ('\nProduto',[produtos],':ERRO AO CARREGAR PRODUTO\n')
                with open ('LogErros','a') as file:
                    file.write('Erro ao carregar o produto',[produtos],'do departamento: ',url)
            produtos+=1
            contadorProdDepart += 1
    arquivo_descrip.close
    arquivo_HTML.close
    arquivo_titulos.close
    arquivo_linksTotal.close
    arquivo_Erros.close
    print ('Total de Produtos:',qntProdutos)
        
def get_title(item_url,iteration):
    source_code = requests.get(item_url) #coleta todo HTML daquela página
    plain_text = source_code.text #transforma o HTML em texto
    soup = BeautifulSoup(plain_text, "lxml") #convertendo o conteúdo em um BeautifulSoup object e armazenando ele no soup
#    if iteration==1:
#        HTML='HTML'+str(iteration)+'\n'    
#    else:
#        HTML='\n\n\nHTML'+str(iteration)+'\n'
#    prod_prettify=prod.prettify(formatter='html')
#    with open ('TotalHTML','a') as file: #ver se vale a pena colocar todo HTML em um arquivo só. NAO PRECISO DO HTML
#        file.write(HTML+'\n')
#        file.write(prod_prettify)
    prod=soup.find('div', {'id': 'content_tab1'})
    Titulo=soup.find('h1',{'id':'newTitleBarClose'}).get_text() #Título, usar .get_text() ou .string ou .text
    Titulo=" ".join(Titulo.split())
    with open ('Dados','a') as file: 
#            try:
        print ('\nProduto',[iteration],Titulo,'\n') #Para Debugar
        file.write(Titulo+'\n\n')
        file.write('\nDENOVO\n')
#            except:
#                file.write('ERRO AO CARREGAR O Título\n\n')
#                print ('\nProduto',[iteration],':ERRO AO CARREGAR TITULO\n')
    Pe(prod)
#    with open ('Dados','a') as file:
#        file.write('\nDENOVO\n')
    Ul(prod)
    if Pe(prod)=='erroPe':
        with open ('Titulos', 'a') as file:
            file.write('DEU ERRO PE - '+Titulo+'\n')
    elif Ul(prod)=='erroUl':
        with open ('Titulos', 'a') as file:
            file.write('DEU ERRO UL - '+Titulo+'\n')
    else:
        with open ('Titulos', 'a') as file:
            file.write('              '+Titulo+'\n')
    with open ('Dados','a') as file:
        file.write('-------------------------------------------------------------------------\n\n')
#Pes
def Pe(prod): #Não Estruturados
    try:
        Pes=prod.find_all('p') #PRINTS #bs4.element.ResultSet
        with open ('Dados','a') as file:
#            i=0
            for p in Pes:
                if p.text=='' or p.text==None:
                    pass
                elif p.text=='Destaques':
                    write=p.text+'\n\n'
                    file.write(write)
                else:
                    for k in range(len(p.contents)):
                        if p.contents[k].name=='br':
                            pass
                        elif p.contents[k].name=='b': 
                            if p.contents[k].text=='Características' or p.contents[k].text=='Caracteristicas' or p.contents[k].text=='Especificacoes Tecnicas' or p.contents[k].text=='Especificações Técnicas' or p.contents[k].text=='Especificações Técnicas ' or p.contents[k].text=='Dimensões e Peso ' or p.contents[k].text=='Dimensões e Peso' or p.contents[k].text=='Dimensoes e Peso' or p.contents[k].text=='Itens Inclusos' or p.contents[k].text=='Destaques ' or p.contents[k].text=='Título' or p.contents[k].text=='Texto' or p.contents[k].text=='Movimento Planetário' or p.contents[k].text=='3 batedores de metal' or p.contents[k].text=='Função Corta Pingos ' or p.contents[k].text=='Base Durilium' or p.contents[k].text=='Tipos de Bebidas' or p.contents[k].text=='Importante' or p.contents[k].text=='Dispositivos de Segurança' or p.contents[k].text=='Softwares Inclusos' or p.contents[k].text=='Dimensoes do Nicho' or p.contents[k].text=='Certificação Inmetro' or p.contents[k].text=='A Marca' or p.contents[k].text=='Montagem e Restrição de Entrega' or p.contents[k].text=='Instalação do Produto' or p.contents[k].text=='Principais Características' or p.contents[k].text=='Outras Características' or p.contents[k].text=='Acessórios Inclusos' or p.contents[k].text=='Aplicativos Inclusos': 
#                                print ('P',[i],':\n',p.contents[k].text,'\n')
                                write='\n'+p.contents[k].text+'\n\n'
                                file.write(write)
                            elif p.contents[k].text=='Serviço de Instalação e Orientação de Uso' or p.contents[k].text=='Restrição de Entrega' or p.contents[k].text=='':
                                pass
                            else:
#                                print ('P',[i],':\n',p.contents[k].text,'\n')
                                write='\n    '+p.contents[k].text+'\n\n'
                                file.write(write)
#                            i+=1
                        elif p.contents[k].name=='i' or p.contents[k].name=='u':
#                            pass
#                            print ('P',[k],':\n',p.contents[k].text,'\n')
                            write='        '+p.contents[k].text+'\n\n'
                            file.write(write)
#                            i+=1
#                        elif p.contents[k].name=='u':
#                            pass
                        else:
#                            print ('P',[i],':\n',p.contents[k],'\n')
                            write='        '+p.contents[k]+'\n'
                            file.write(write)
#                            i+=1
    except:
        return 'erroPe'
#ULs
def Ul(prod): #Estruturados
    try:
        Uls=prod.find('ul')
        Lis=Uls.find_all('li')
        with open ('Dados','a') as file:
            i=0
            file.write('\n')
            for li in Lis:
                spansKey=li.find_all('span')[0].text
                spansKey=" ".join(spansKey.split())
                file.write(spansKey+'\n')
#                print ('span1:',spansKey)
                spansValue=li.find_all('span')[1].text
                spansValue=" ".join(spansValue.split())
                file.write(spansValue+'\n\n')
#                print ('span2:',spansValue,'\n')      
                i+=1
    except:
        return 'erroUl'
FastShop(30)
end=time.time()
print ('Durou:',end-start,'segundos\n')
#segPorProd=(end-start)/qntProdutos
#print ('Demorou:',segPorProd,'Segundos/Produto')

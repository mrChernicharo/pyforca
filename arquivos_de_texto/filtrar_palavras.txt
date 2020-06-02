"""
Esse é o arquivo responsável por 
1. extraír as palavras e dicas do arquivo banco_palavras.txt
2. filtrar linhas e espaços
3. agrupar palavras e dicas em duas listas que serão usadas na hora de sortear as palavras
"""


# declaração global de variáveis
palavra = []
arr_letras = []
arr_palavras = []

dica =[]
arr_dicas = []
arr_dicas_letras = []


def filtrar_palavras(): 
    # abrir arquivo .txt 
    banco = open('banco_palavras.txt','r')

    #armazenar linhas em uma lista
    linhas = banco.readlines()
    # print(linhas) 
   
    # armazenar letras de palavras 
    for linha in linhas:
        palavra.clear()

        for ch in linha:
            # se encontrar vírgula, quebre o laço 
            if ch == ',' :
                break
            else:
                palavra.append(ch)

        arr_letras.append(palavra.copy())


    # armazenar letras de dicas 
    for linha in linhas:
        leitura = False
        dica.clear()
        
        for ch in linha:
            if leitura == False:
                pass
            # se encontrar vírgula, comece a leitura
            if ch == ',':  
                leitura = True
                continue
                
                # se encontrar \n quebre o laço
                if ch == '\n':
                    leitura = False
                    break
            else:
                # acrescente letras à dica
                if leitura and ch != '\n':     
                    dica.append(ch)
                    
        dica.pop(0) # <== remover espaço vazio na primeira posição da dica       
        arr_dicas_letras.append(dica.copy())


    # agrupar letras em palavras e armazenar em arr_palavras
    for i in range(len(arr_letras)):
        palavra_filtrada = ''
        for ch in arr_letras[i]:
            palavra_filtrada += ch

        arr_palavras.append(palavra_filtrada)


    # agrupar letras das dicas e armazenar em arr_dicas
    for i in range(len(arr_dicas_letras)):
        palavra_filtrada = ''
        for ch in arr_dicas_letras[i]:
            palavra_filtrada += ch

        arr_dicas.append(palavra_filtrada)

    # Para testar e verificar palavras e dicas:
    # 1. descomente os prints 
    # print(arr_palavras)    
    # print(arr_dicas) 

    return ([arr_palavras, arr_dicas])

    # fechar arquivo de texto
    banco.close()

# 2. descomente a chamada da função
# filtrar_palavras()

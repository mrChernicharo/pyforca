banco = open('banco_palavras.txt','r')
linhas = banco.readlines()


palavra = []
arr_letras = []
arr_palavras = []

dica =[]
arr_dicas = []
arr_dicas_letras = []

print('-----' * 10)    

for linha in linhas:
    print(linha.rstrip())
    palavra.clear()

    for ch in linha:
        if  ch == ' ' or  ch == ',' or ch == '\n':
            break
        else:
            palavra.append(ch)

    arr_letras.append(palavra.copy())
    print(arr_letras)



for linha in linhas:
    leitura = False
    dica.clear()
    
    for ch in linha:
        if leitura == False:
            pass
        if ch == ',':  
            leitura = True
            continue
        
            if ch == '\n':
                leitura = False
                break
        else:
            if leitura and ch != '\n':     
                dica.append(ch)
                
    arr_dicas_letras.append(dica.copy())
    # print(dica) 

print(arr_dicas_letras)

print('-----' * 10)    

print(arr_letras)    
print(arr_letras[0])

for i in range(len(arr_letras)):
    palavra_filtrada = ''
    for ch in arr_letras[i]:
        palavra_filtrada += ch

    print(palavra_filtrada)
    arr_palavras.append(palavra_filtrada)
print(arr_palavras)    


for i in range(len(arr_dicas_letras)):
    palavra_filtrada = ''
    for ch in arr_dicas_letras[i]:
        palavra_filtrada += ch

    print(palavra_filtrada)
    arr_dicas.append(palavra_filtrada)
print(arr_dicas) 

    

banco.close()
from sortear_palavra import sortear_palavras
from render_forca import render_forca
from time import sleep

sorteio = sortear_palavras()

palavra = sorteio[0]
dica = sorteio[1]
        
palavra_oculta = []
arr_tentativas = []

letras_alfabeto = ['a', 'b', 'c',  'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# print(f'palavra secreta: {palavra}') 

def painel_letras(palavra_secreta, erros):
       
    letras_painel = ''
    palavra_oculta.clear()
    resposta = ''



    # checar se letra escolhida coincide com palavra secreta
    for l in palavra_secreta:
        if l in arr_tentativas:
            palavra_oculta.append(l)
        else:
            palavra_oculta.append('_')

    for l in palavra_oculta:
        resposta += l + ' '
    print(f'resposta: {resposta}')  


    # print(f'palavra_oculta: {palavra_oculta}')  

    # ajustar painel de letras conforme letras restantes
    selecione = True
    letras_painel = ''
    count = 0
    for j in letras_alfabeto:
        letras_painel += j
        letras_painel += ' '
        count += 1
        if count % 5 == 0:
            letras_painel += '\n'

    # printar painel
    print(f'\033[36m{letras_painel}\033[m')

    # selecionar letra
    while selecione:
        tentativa = input('escolha uma letra: ')

        # checar se letra é válida
        if tentativa not in letras_alfabeto:
            print('\033[31mopção inválida. Tente novamente\n\033[m')
            break
        else:
            selecione = False

        arr_tentativas.append(tentativa)


        if tentativa in palavra_secreta:
            print('acertou! \n')
            sleep(0.6)
        else:
            print(f'\033[31merrou!\n\033[m')  
            erros += 1
            sleep(0.6)



        # remover letras já escolhidas do painel   
        for l in letras_alfabeto:
            if tentativa == l:
                letras_alfabeto.remove(tentativa)

        # print(f'erros: {erros}')    
        # print(erros)
    

        return (erros) 
           

                                    

# painel_letras(palavra)




#'\033[36m\na b c d e f \ng h i j k l \nm n o p q r s \nt u v w x y z \033[m'

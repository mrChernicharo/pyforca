from time import sleep 
from render_forca import render_forca
from sortear_palavra import sortear_palavras
# from painel_letras import painel_letras

new_game = False
game_loop = True
inicio = True
erros = 0

sorteio = sortear_palavras()

palavra_secreta = sorteio[0]
dica = sorteio[1]

palavra_oculta = []
arr_tentativas = []
letras_alfabeto = ['a', 'b', 'c',  'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def painel_letras(palavra_secreta, erros, new_game):
    
    letras_painel = ''
    palavra_oculta = []
    resposta = ''
    arr_tentativas = []

    if new_game:
        palavra_oculta.clear()
        arr_tentativas.clear()



    # checar se letra escolhida coincide com palavra secreta
    for l in palavra_secreta:
        if l in arr_tentativas:
            palavra_oculta.append(l)
        else:
            palavra_oculta.append('_')

    for l in palavra_oculta:
        resposta += l + ' '
    print(f'resposta: {resposta}')  




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


    return (erros) 







# main_loop
while game_loop:
    #início da partida
    while inicio == True:
        erros = 0
        print('Bem vindo ao jogo da forca!')
        sleep(0.6)
        print(f'Atenção à dica:')
        sleep(0.6)
        print('')
        print(f'A dica é: " {dica}" \n')
        sleep(0.6)
        print('preparado?')
        sleep(0.6)
        print('')
        sleep(1)
        inicio =  False

    # jogo
    while int(erros) <= 5:    
        render_forca(erros) 
        # print(painel_letras(palavra_secreta, erros))

        erros = painel_letras(palavra_secreta, erros, new_game)
        print(f'erros: {erros}')
        new_game = False


    
    # game over
    while int(erros) >= 6:
        render_forca(erros) 
        sleep(0.6)
        game_over = input('deseja jogar novamente? [s/n] ')    
        print(f'arr_tentativas: {arr_tentativas}')
        print(f'palavra_oculta: {palavra_oculta}')
        palavra_oculta.clear()
        arr_tentativas.clear()

        if game_over == 's':
            inicio = True
            game_loop = True
            erros = 0
            sorteio = sortear_palavras()
            palavra_secreta = sorteio[0]
            dica = sorteio[1]
            new_game = True
                    
        elif game_over == 'n':
            game_loop = False
            break
        else:    
            print ('opçao invalida.')    



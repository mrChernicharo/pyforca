from time import sleep 
from render_forca import render_forca
from sortear_palavra import sortear_palavras
from painel_letras import painel_letras

game_loop = True
inicio = True
erros = 0

sorteio = sortear_palavras()

palavra_secreta = sorteio[0]
dica = sorteio[1]




# main_loop
while game_loop:
    #início da partida
    while inicio:
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
    while int(erros) < 6:    
        render_forca(erros) 
        # print(painel_letras(palavra_secreta, erros))

        erros = painel_letras(palavra_secreta, erros)
        print(f'erros: {erros}')


    
    # game over
    while int(erros) >= 6:
        game_over = input('deseja jogar novamente? [s/n] ')    

        if game_over == 's':
            inicio = True
            game_loop = True
            erros = 0
            sorteio = sortear_palavras()
            palavra_secreta = sorteio[0]
            dica = sorteio[1]
            break
        elif game_over == 'n':
            game_loop = False
            break
        else:    
            print ('opçao invalida.')    



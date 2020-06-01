from time import sleep 
from render_forca import render_forca
from sortear_palavra import sortear_palavras
from painel_letras import painel_letras

game_loop = True
erros = 0

sorteio = sortear_palavras()

palavra = sorteio[0]
dica = sorteio[1]


print('Bem vindo ao jogo da forca!')
sleep(1)
print(f'Atenção à dica:')
sleep(1)
print('')
print(f'A dica é: " {dica}" \n')
sleep(1)
print('preparado?')
sleep(1)
print('')
sleep(1)

# main_loop
while game_loop:
    
    erros += 1
    render_forca(erros)
    input('aperte enter')
    print(painel_letras())

    
    # game over
    while erros > 6:
        game_over = input('deseja jogar novamente? [s/n] ')    

        if game_over == 's':
            game_loop = True
            erros = 0
            break
        elif game_over == 'n':
            game_loop = False
            break
        else:    
            print ('opçao invalida.')    



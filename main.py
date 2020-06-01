from time import sleep 
from render_forca import render_forca

game_loop = True
erros = 0



while game_loop:
    render_forca(erros)
    erros += 1
    input('aperte enter')
    
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



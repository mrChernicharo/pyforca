"""
Arquivo principal

É só rodar e se divertir jogando o PyForca!
"""

from time import sleep
from sortear_palavra import sortear_palavras
from render_forca import render_forca
from unicodedata import normalize


# sortear e registrar palavra e dica
sorteio = sortear_palavras()
palavra_secreta = sorteio[0]
# palavra_secreta = 'monções'
dica = sorteio[1]

# variáveis globais
erros = 0
game = True
partida = True
inicio = True
partidas = 1
vitorias = 0
derrotas = 0
palavra_oculta = []
arr_tentativas = []
letras_alfabeto = ['a', 'b', 'c',  'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
resposta = ''
letras_painel = ''

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def exibirPlacar():
    sleep(0.6)
    print(f'partida: {partidas}')
    print(f'vitorias: {vitorias}')
    print(f'derrotas: {derrotas}')
    sleep(0.6)

def pontinho():
    j = 14
    for i in range(30):   
        sleep(0.04)
        if i < 14:
            print('. ' * i)
        if i >= 15:
            print('. ' * (j))
            j -= 1

            


# apresentação
print('\033[32mSeja bem vindo ao PyForca!\033[m')
sleep(1.2)
print('Um game de\033[32m Felipe Chernicharo\033[m')
pontinho()
nome = input('Digite o seu nome ').capitalize()
print(f'\033[32mVamos nessa! {nome}\n\033[m')
sleep(0.8)

#loop principal
while game:

    # introdução da partida
    while inicio:
        erros = 0
        print(f'\033[32m\nIniciando partida {partidas}!\n\033[m')
        sleep(1)
        print(f'Atenção à dica:')
        sleep(0.6)
        print('')
        print(f'A dica é: \033[35m" {dica.capitalize()}" \n\033[m')
        sleep(1.2)
        print('preparado?')
        sleep(0.6)
        print('')
        sleep(1)
        inicio =  False
    
    # imprimir forca
    if erros < 6:
        render_forca(erros)

    # fluxo de derrota    
    if erros == 6:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|         -|-     ')
        print('|         / \     ')
        print('|           ')
        print('|        ')
        print('|')
        pontinho()
        print(f'\033[31mLamento {nome}! Você Perdeu! \033[m')
        sleep(1.2)
        print(f'A palavra screta é {palavra_secreta.upper()}')
        sleep(1.2)
        derrotas += 1
        partida = False
        exibirPlacar()

    if not resposta:
        print('resposta: ' + '_ ' * len(palavra_secreta))
    else:    
        if erros < 6:
            print(f'resposta: {resposta}')  

    # loop da partida
    while partida:
        
        letras_painel = ''
        count = 1
        for l in letras_alfabeto:
            letras_painel += l + ' '
            if count % 6 == 0:
                letras_painel += '\n'
            count += 1    
        print(f'\033[36m{letras_painel.upper()}\033[m')  
            
        tentativa = input('escolha uma letra: ')
        if tentativa not in letras_alfabeto:
            print('\033[31mOpção inválida. Escolha uma letra que ainda não tenha sido selecionada\n\033[m')
            sleep(0.6)
            break
        else: 
            letras_alfabeto.remove(tentativa)
        
        # registrar tentativas
        arr_tentativas.append(tentativa)


        # preencher palavra oculta e resposta 
        palavra_oculta.clear()
        resposta = ''

        # ajustes de acentuação
        for l in palavra_secreta:
                               
            # ajustar palavra oculta
            if remover_acentos(l) in arr_tentativas:
                palavra_oculta.append(l)
            else:
                palavra_oculta.append('_')
            
        # ajustar resposta
        for l in palavra_oculta:
            resposta += l + ' '


        # fluxo de acerto, erro e vitória
        if remover_acentos(tentativa) in remover_acentos(palavra_secreta):
            print('\033[33macertou! \n\033[m')


            if not '_' in palavra_oculta:
                pontinho()
                print(f'\033[33mParabéns {nome}! Você venceu!!! \033[m\nA palavra secreta é {palavra_secreta.upper()}')
                vitorias += 1
                partida = False
                sleep(0.8)
                exibirPlacar()
                break     

            break

        else:
            print(f'\033[31merrou!\n\033[m')  
            erros += 1
            sleep(0.6)
            break

        if erros >= 6:
            partida = False
            break

    # final da partida
    while not partida:

        game_over= input('Deseja jogar novamente? [s/n] ')

        if game_over == 's':
            erros = 0
            partidas += 1
            aux = ''
            arr_tentativas.clear()
            sorteio = sortear_palavras()
            palavra_secreta = sorteio[0]
            # palavra_secreta = 'monções'
            resposta = ''
            dica = sorteio[1]
            letras_alfabeto = ['a', 'b', 'c',  'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            inicio = True
            partida = True


                    
        elif game_over == 'n':
            game = False
            print (f'\033[32mAté logo {nome}!\033[m')    
            break
        else:    
            print (f'\033[32mOps...Opçao invalida.\033[m')    

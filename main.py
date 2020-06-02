from time import sleep
from sortear_palavra import sortear_palavras

# sortear e registrar palavra e dica
sorteio = sortear_palavras()
palavra_secreta = sorteio[0]
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


def exibirPlacar():
    sleep(0.6)
    print(f'partida: {partidas}')
    print(f'vitorias: {vitorias}')
    print(f'derrotas: {derrotas}')
    sleep(0.6)


print('Seja bem vindo ao PyForca!')
nome = input('Digite o seu nome ')

while game:

    while inicio:
        erros = 0
        print(f'Iniciando partida {partidas}!')
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
    
    # imprimir forca
    if erros == 0:
        print('------------     ')
        print('|          |   ')
        print('|             ')
        print('|               ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if erros == 1:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|               ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if erros == 2:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|          |     ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if erros == 3:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|         -|     ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if erros == 4:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|         -|-     ')
        print('|                ')
        print('|           ')
        print('|         ')
        print('|         ')
    if erros == 5:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|         -|-     ')
        print('|         /      ')
        print('|           ')
        print('|         ')
        print('|         ')
    if erros == 6:
        print('------------     ')
        print('|          |   ')
        print('|          0   ')
        print('|         -|-     ')
        print('|         / \     ')
        print('|           ')
        print('|        ')
        print('|')
        print(f'Lamento {nome}! Você Perdeu! ')
        print(f'A palavra screta é {palavra_secreta.upper()}')
        derrotas += 1
        partida = False
        exibirPlacar()

    if not resposta:
        print('resposta: ' + '_ ' * len(palavra_secreta))
    else:    
        if erros < 6:
            print(f'resposta: {resposta}')  

    while partida:
        
        letras_painel = ''
        for l in letras_alfabeto:
            letras_painel += l
        print(letras_painel)  
            
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
            aux = ''
            if l == 'á' or l == 'ã' or l == 'â' or l == 'à':
                aux = 'a'
            if l == 'ç':
                aux = 'c' 
            if l == 'é' or l == 'ê':
                aux = 'e'     
            if l == 'ó' or l == 'ô' or l == 'õ':
                aux = 'o' 
            if l == 'í':
                aux = 'i'  
                               
            # ajustar palavra oculta
            if l in arr_tentativas:
                palavra_oculta.append(l)
            elif aux in arr_tentativas:
                palavra_oculta.append(l) 
            else:
                palavra_oculta.append('_')
            
        # ajustar resposta
        for l in palavra_oculta:
            if aux:
                resposta += aux + ' '

            else:
                resposta += l + ' '


        # fluxo de acerto e erro
        if tentativa in palavra_secreta:
            print('acertou! \n')


            if not '_' in palavra_oculta:
                print(f'Parabéns {nome}! Você venceu!!! \nA palavra secreta é {palavra_secreta.upper()}')
                vitorias += 1
                partida = False
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
            print (f'Até logo {nome}!')    
            break
        else:    
            print ('opçao invalida.')    

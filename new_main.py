from time import sleep
from sortear_palavra import sortear_palavras

sorteio = sortear_palavras()

# palavra_secreta = sorteio[0]
palavra_secreta = 'monções'
dica = sorteio[1]

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




# nome = input('Qual o seu nome? ')
nome = 'Zé'

while game:

    # while inicio:
    #     erros = 0
    #     print(f'Iniciando partida {partidas}!')
    #     sleep(0.6)
    #     print(f'Atenção à dica:')
    #     sleep(0.6)
    #     print('')
    #     print(f'A dica é: " {dica}" \n')
    #     sleep(0.6)
    #     print('preparado?')
    #     sleep(0.6)
    #     print('')
    #     sleep(1)
    #     inicio =  False


    print(palavra_secreta)
    print(dica)
    print(f'partidas: {partidas}')
    print(f'vitorias: {vitorias}')
    print(f'derrotas: {derrotas}')
    print(f'palavra_oculta: {palavra_oculta}')
    print(f'resposta: {resposta}')  

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
        print(' Lamento! Você Perdeu! ')
        
        derrotas += 1
        partida = False


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



        
        arr_tentativas.append(tentativa)
        print(arr_tentativas)

        # preencher palavra oculta e resposta 
        acentuacao = False
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
                               
            print(aux)

            if l in arr_tentativas:
                palavra_oculta.append(l)
            elif aux in arr_tentativas:
                palavra_oculta.append(l)
                acentuacao = True
   
            else:
                palavra_oculta.append('_')

        for l in palavra_oculta:
            if aux:
                resposta += aux + ' '

            else:
                resposta += l + ' '


        if acentuacao:
            print('acertou! \n')           
            break



            if not '_' in palavra_oculta:
                print('Parabéns {nome}! Você venceu!!!')
                vitorias += 1
                partida = False

            sleep(0.6)
            break        

        else:
            print(f'\033[31merrou!\n\033[m')  
            erros += 1
            sleep(0.6)
            break

        if erros >= 6:
            partida = False
            break




        if not acentuacao:    
            if tentativa in palavra_secreta:
                print('acertou! \n')
                break


                if not '_' in palavra_oculta:
                    print('Parabéns {nome}! Você venceu!!!')
                    vitorias += 1
                    partida = False

                sleep(0.6)
                break        

            else:
                print(f'\033[31merrou!\n\033[m')  
                erros += 1
                sleep(0.6)
                break

            if erros >= 6:
                partida = False
                break


    while not partida:
        game_over= input('Deseja jogar novamente? [s/n] ')

        if game_over == 's':
            erros = 0
            partidas += 1
            arr_tentativas.clear()
            sorteio = sortear_palavras()
            palavra_secreta = sorteio[0]
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

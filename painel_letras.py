from sortear_palavra import sortear_palavras

sorteio = sortear_palavras()

palavra = sorteio[0]
dica = sorteio[1]
        
palavra_oculta = []
arr_tentativas = []



def painel_letras(palavra_secreta):
    while True:

        letras_alfabeto = ['a', 'b', 'c',  'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        letras_painel = ''
        i = 0
        print(f'palavra secreta: {palavra_secreta}')


        # ajustar painel de letras conforme letras restantes
        selecione = True
        letras_painel = ''
        count = 0
        for j in letras_alfabeto:
            letras_painel += j
            letras_painel += ' '
            count += 1
            if count % 6 == 0:
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

        # remover letras já escolhidas do painel   
        for l in letras_alfabeto:
            if tentativa == l:
                letras_alfabeto.remove(tentativa)
        
        # checar se letra escolhida coincide com palavra secreta
        for l in palavra_secreta:
            if l in arr_tentativas:
                palavra_oculta.append(l)
            else:
                palavra_oculta.append('_')
        print(f'palavra_oculta: {palavra_oculta}') 

        # exibir palavra oculta
        resposta = ''
        for l in palavra_oculta:
            resposta += l + ' '
        print(f'resposta: {resposta}')    

        if tentativa in palavra_secreta:
            print('acertou!')
        else:
            print('errou!')    
                
        # tentativa = input('digite uma letra ')
        arr_tentativas.append(tentativa)
        print(f'arr_tentativas: {arr_tentativas}')
    # print(painel_palavra(palavra_secreta, tentativa))



        # print(letras_alfabeto)    


# print(palavra_secreta)

# def painel_palavra(palavra_secreta, tentativa):
#     palavra_oculta = []
#     print(arr_tentativas)
    
#     # print(palavra_secreta)
#     # print(tentativa)

#     # checar se letra escolhida coincide com palavra secreta
#     for l in palavra_secreta:
#         if l in arr_tentativas:
#             palavra_oculta.append(l)
#         else:
#             palavra_oculta.append('_')
#     print(palavra_oculta) 

#     # exibir palavra oculta
#     resposta = ''
#     for l in palavra_oculta:
#         resposta += l + ' '
#     print(resposta)    

#     if tentativa in palavra_secreta:
#         print('acertou!')
#     else:
#         print('errou!')    
            
#     tentativa = input('digite uma letra ')
#     arr_tentativas.append(tentativa)
#     print(painel_palavra(palavra_secreta, tentativa))


painel_letras(palavra)




#'\033[36m\na b c d e f \ng h i j k l \nm n o p q r s \nt u v w x y z \033[m'

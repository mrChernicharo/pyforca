from sortear_palavra import sortear_palavras

sorteio = sortear_palavras()

palavra = sorteio[0]
dica = sorteio[1]

def painel_letras():

    letras_alfabeto = ['a', 'b', 'c',  'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    letras_painel = ''
    i = 0

    while True:
        selecione = True
        letras_painel = ''

        while selecione:
            tentativa = input('escolha uma letra: ')
            if tentativa not in letras_alfabeto:
                print('\033[31mopção inválida. Tente novamente\033[m')
                break
            else:
                selecione = False

        # remover letras já escolhidas    
        for l in letras_alfabeto:
            if tentativa == l:
                letras_alfabeto.remove(tentativa)

        # ajustar painel de letras conforme letras restantes
        count = 0
        for j in letras_alfabeto:
            letras_painel += j
            letras_painel += ' '
            count += 1
            if count % 6 == 0:
                letras_painel += '\n'
    



        print(f'\033[36m{letras_painel}\033[m')
        # print(letras_alfabeto)    
        







#'\033[36m\na b c d e f \ng h i j k l \nm n o p q r s \nt u v w x y z \033[m'

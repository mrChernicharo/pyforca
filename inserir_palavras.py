"""
Rode esse arquivo para inserir novas palavras no banco de palavras
"""
ativo = True

while ativo:
    print('--------' * 10)
    palavra = input('digite uma nova palavra: ')
    dica = input('digite uma dica para a palavra: ')


    # escrever palavras e dicas no arquivo de texto
    banco = open('banco_palavras.txt','a')
    banco.write(f'{palavra}, {dica} \n')
    banco.close()

    checkout = True
    while checkout:
        resposta = input('Deseja inserir mais uma palavra? [s/n] ')
        if resposta == 's':
            checkout = False
            break
        elif resposta == 'n':
            checkout = False
            ativo = False
        else:
            print('\033[31mNão entendi sua resposta. \033[m')

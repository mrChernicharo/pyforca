palavra = input('digite uma nova palavra: ')
dica = input('digite uma dica para a palavra: ')


# escrever palavras e dicas no arquivo de texto
banco = open('AP3/banco_palavras.txt','a')
banco.write(f'{palavra}, {dica} \n')
banco.close()
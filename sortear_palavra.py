from filtrar_palavras import filtrar_palavras
from random import randint

def sortear_palavras():
    # receber lista de palavras e dicas
    listas = filtrar_palavras()

    lista_palavras = listas[0]
    lista_dicas = listas[1]

    # criar número aleatório entre zero e a quantidade de itens na lista de palavras
    numero_aleatorio = randint(0, len(lista_palavras) - 1)

    palavra_sorteada = lista_palavras[numero_aleatorio]
    dica = lista_dicas[numero_aleatorio]
    # print(palavra_sorteada, dica)


    return([palavra_sorteada, dica])
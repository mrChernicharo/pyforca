from filtrar_palavras import filtrar_palavras
from random import randint

# receber lista de palavras e dicas
listas = filtrar_palavras()

lista_palavras = listas[0]
lista_dicas = listas[1]


# criar número aleatório entre zero e a quantidade de itens na lista de palavras
numero_aleatorio = randint(0, len(lista_palavras) - 1)


print(lista_palavras[numero_aleatorio])
print(lista_dicas[numero_aleatorio])
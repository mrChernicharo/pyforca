from filtrar_palavras import filtrar_palavras
from random import randint

lista = filtrar_palavras()

lista_palavras = lista[0]
lista_dicas = lista[1]

# print(lista_palavras[2])
# print(lista_dicas[2])

numero_aleatorio = randint(0, len(lista_palavras) - 1)

print(numero_aleatorio)
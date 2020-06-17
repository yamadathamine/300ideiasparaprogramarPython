# encoding: utf-8 
# usando python 3
# Subcadeias - Escreva um programa que lê uma cadeia de caracteres de tamanho 20, 
# separa-a em duas e mostra na tela as duas metades.

frase = input("Digite uma frase com 20 caracteres: ")

tamanho=len(frase)
metade = int(tamanho/2)
print(frase[0:metade])
print(frase[metade:tamanho-1])

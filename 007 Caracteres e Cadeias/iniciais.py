# encoding: utf-8 
# usando python 3
# Iniciais - Escreva um programa que lê nome e sobrenome, e mostra na tela as iniciais.


nome_completo = input("Digite o seu primeiro e segundo nome: ")

nomes = nome_completo.split(" ")

print(nomes[0][0])
print(nomes[1][0])


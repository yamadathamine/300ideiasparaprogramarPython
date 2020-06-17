# encoding: utf-8 
# usando python 3
# Finais - Reescreva o programa anterior para mostrar na tela as letras finais do nome e
# sobrenome.

nome_completo = input("Digite o seu primeiro e segundo nome: ")

nomes = nome_completo.split(" ")

print(nomes[0][len(nomes[0])-1])
print(nomes[1][len(nomes[1])-1])

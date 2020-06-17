# encoding: utf-8 
# usando python 3
# Menu posicionado - Implemente um programa que mostra um menu a partir de uma linha lida do teclado

import os

os.system('clear')
linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))

print("\033["+str(linha)+";"+str(coluna)+"H Menu relatórios")
linha += 1
print("\033["+str(linha)+";"+str(coluna)+"H 1 - Por nome")
linha += 1
print("\033["+str(linha)+";"+str(coluna)+"H 2 - Por código")
linha += 1
print("\033["+str(linha)+";"+str(coluna)+"H 3 - Por data")
linha += 1
print("\033["+str(linha)+";"+str(coluna)+"H 4 - Fim")
linha += 2
teste=input("\033["+str(linha)+";"+str(coluna)+"HOpção: ")
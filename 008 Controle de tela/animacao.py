# encoding: utf-8 
# usando python 3
# Animação horizontal - Faça um programa que lê valores de linha e coluna e desenha um "O" 
# na posição lida, e depois faz o seguinte, esperando uma tecla para cada ação (sempre na mesma linha):
# - apaga o 'O' da posição atual
# - incrementa a coluna
# - mostra o 'O' na nova posição
# E assim sucessivamente por 10 colunas.

import os
 
os.system('clear')

linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))

print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")
input("")
os.system('clear')
coluna += 1;
print("\033["+str(linha)+";"+str(coluna)+"HO")

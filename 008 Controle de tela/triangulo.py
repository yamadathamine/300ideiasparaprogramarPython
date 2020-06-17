# encoding: utf-8 
# usando python 3
# Triângulo com iniciais - Faça um programa que lê valores de linha e coluna, 
# além das iniciais de um nome (até 3 caracteres) e desenha um triângulo ("bole" o desenho) 
# com um vértice na linha e coluna lidas e com as iniciais dentro.
import os
 
os.system('clear')
linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))
iniciais = input("Digite as suas iniciais (até 3 caracteres): ")

print("\033["+str(linha)+";"+str(coluna)+"H#")
linha += 1
coluna -= 1
print("\033["+str(linha)+";"+str(coluna)+"H# #")
linha += 1
coluna -= 1
print("\033["+str(linha)+";"+str(coluna)+"H#"+iniciais+"#")
linha += 1
coluna -= 1
print("\033["+str(linha)+";"+str(coluna)+"H#     #")
linha += 1
coluna -= 1
print("\033["+str(linha)+";"+str(coluna)+"H#       #")
linha += 1
coluna -= 1
print("\033["+str(linha)+";"+str(coluna)+"H###########")

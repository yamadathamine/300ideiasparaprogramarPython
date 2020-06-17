# encoding: utf-8 
# usando python 3
# Quadrado em posição - Escrever um programa que desenha um quadrado com o canto superior 
# esquerdo em uma linha e coluna lidas. O caractere usado para formar o quadrado é o '#'. 
# Veja abaixo uma sugestão para a tela do programa.

import os
 
os.system('clear')

print("Este programa desenha um quadrado com o caractere #")
linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))

print("\033["+str(linha)+";"+str(coluna)+"H##########")
linha += 1
print("\033["+str(linha)+";"+str(coluna)+"H#        #")
linha += 1
print("\033["+str(linha)+";"+str(coluna)+"H#        #")
linha += 1
print("\033["+str(linha)+";"+str(coluna)+"H#        #")
linha += 1
print("\033["+str(linha)+";"+str(coluna)+"H##########")
input("Pressione qualquer tecla")
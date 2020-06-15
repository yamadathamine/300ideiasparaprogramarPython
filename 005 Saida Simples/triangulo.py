# encoding: utf-8 
# usando python 3
# Triângulo com iniciais - Escrever um programa que lê um caractere, 
# as iniciais de um nome (3 caracteres), uma linha e uma coluna e depois 
# desenha na tela um triângulo equilátero formado com o caractere, 
# tendo dentro as iniciais lidas. O caractere no ápice do triângulo deve estar 
# na linha e coluna lidas, e a altura do triângulo deve ser no máximo 5 linhas.
import os

caractere = input("Caractere: ")
iniciais = input("Iniciais(3 letras): ")
l_inicial = input("Linha: ")
c_inicial = input("Coluna: ")

os.system('clear')
linha = int(l_inicial)
coluna = int(c_inicial)
print("\033["+str(linha)+";"+str(coluna)+"H"+caractere)
linha+=1
coluna = int(c_inicial)-1
print("\033["+str(linha)+";"+str(coluna)+"H"+caractere+caractere+caractere)
linha+=1
coluna = int(c_inicial)-2
print("\033["+str(linha)+";"+str(coluna)+"H"+caractere+caractere+caractere+caractere+caractere)
linha+=1
coluna = int(c_inicial)-3
print("\033["+str(linha)+";"+str(coluna)+"H"+caractere+caractere+iniciais+caractere+caractere)
linha+=1
coluna = int(c_inicial)-4
print("\033["+str(linha)+";"+str(coluna)+"H"+caractere+caractere+caractere+caractere+caractere+caractere+caractere+caractere+caractere)

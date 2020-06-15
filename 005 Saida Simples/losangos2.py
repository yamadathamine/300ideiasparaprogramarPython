# encoding: utf-8 
# usando python 3
# Losangos 2 - No programa do exercício anterior, 
# troque o caractere de forma que os losangos sejam feitos com asteriscos (*).

import os

l_inicial = input("Digite a posicão da linha: ")
c_inicial = input("Digite a posição da coluna: ")
os.system('clear')
linha = int(l_inicial)
coluna = int(c_inicial)
print("\033["+str(linha)+";"+str(coluna)+"H*")
coluna+=15
print("\033["+str(linha)+";"+str(coluna)+"H*")
linha+=1
coluna = int(c_inicial)-1
print("\033["+str(linha)+";"+str(coluna)+"H***")
coluna = int(c_inicial)+14
print("\033["+str(linha)+";"+str(coluna)+"H***")
linha+=1
coluna = int(c_inicial)-2
print("\033["+str(linha)+";"+str(coluna)+"H*****")
coluna = int(c_inicial)+13
print("\033["+str(linha)+";"+str(coluna)+"H*****")
linha+=1
coluna = int(c_inicial)-3
print("\033["+str(linha)+";"+str(coluna)+"H*******")
coluna = int(c_inicial)+12
print("\033["+str(linha)+";"+str(coluna)+"H*******")
linha+=1
coluna = int(c_inicial)-4
print("\033["+str(linha)+";"+str(coluna)+"H*********")
coluna = int(c_inicial)+11
print("\033["+str(linha)+";"+str(coluna)+"H*********")
linha+=1
coluna = int(c_inicial)-3
print("\033["+str(linha)+";"+str(coluna)+"H*******")
coluna = int(c_inicial)+12
print("\033["+str(linha)+";"+str(coluna)+"H*******")
linha+=1
coluna = int(c_inicial)-2
print("\033["+str(linha)+";"+str(coluna)+"H*****")
coluna = int(c_inicial)+13
print("\033["+str(linha)+";"+str(coluna)+"H*****")
linha+=1
coluna = int(c_inicial)-1
print("\033["+str(linha)+";"+str(coluna)+"H***")
coluna = int(c_inicial)+14
print("\033["+str(linha)+";"+str(coluna)+"H***")
linha+=1
coluna = int(c_inicial)
print("\033["+str(linha)+";"+str(coluna)+"H*")
coluna+=15
print("\033["+str(linha)+";"+str(coluna)+"H*")

linha = int(l_inicial) + 15
print("\033["+str(linha)+";0H")
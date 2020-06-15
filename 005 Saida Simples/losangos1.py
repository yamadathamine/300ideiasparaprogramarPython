# encoding: utf-8 
# usando python 3
# Losangos 1 - Implemente um programa que desenhe os losangos abaixo na tela, 
# sendo que o topo do primeiro losango é colocado em uma linha e uma coluna lidas do teclado, 
# e o topo do segundo fica 15 colunas à direita do primeiro.
#                          X 			          X              
#                         XXX 				     XXX	
#						 XXXXX 					XXXXX	
#                       XXXXXXX 			   XXXXXXX	
#                      XXXXXXXXX 			  XXXXXXXXX	
#                       XXXXXXX 			   XXXXXXX	
#                        XXXXX 				    XXXXX
#						  XXX 					 XXX 					
#					       X  				      X  
import os

l_inicial = input("Digite a posicão da linha: ")
c_inicial = input("Digite a posição da coluna: ")
os.system('clear')
linha = int(l_inicial)
coluna = int(c_inicial)
print("\033["+str(linha)+";"+str(coluna)+"HX")
coluna+=15
print("\033["+str(linha)+";"+str(coluna)+"HX")
linha+=1
coluna = int(c_inicial)-1
print("\033["+str(linha)+";"+str(coluna)+"HXXX")
coluna = int(c_inicial)+14
print("\033["+str(linha)+";"+str(coluna)+"HXXX")
linha+=1
coluna = int(c_inicial)-2
print("\033["+str(linha)+";"+str(coluna)+"HXXXXX")
coluna = int(c_inicial)+13
print("\033["+str(linha)+";"+str(coluna)+"HXXXXX")
linha+=1
coluna = int(c_inicial)-3
print("\033["+str(linha)+";"+str(coluna)+"HXXXXXXX")
coluna = int(c_inicial)+12
print("\033["+str(linha)+";"+str(coluna)+"HXXXXXXX")
linha+=1
coluna = int(c_inicial)-4
print("\033["+str(linha)+";"+str(coluna)+"HXXXXXXXXX")
coluna = int(c_inicial)+11
print("\033["+str(linha)+";"+str(coluna)+"HXXXXXXXXX")
linha+=1
coluna = int(c_inicial)-3
print("\033["+str(linha)+";"+str(coluna)+"HXXXXXXX")
coluna = int(c_inicial)+12
print("\033["+str(linha)+";"+str(coluna)+"HXXXXXXX")
linha+=1
coluna = int(c_inicial)-2
print("\033["+str(linha)+";"+str(coluna)+"HXXXXX")
coluna = int(c_inicial)+13
print("\033["+str(linha)+";"+str(coluna)+"HXXXXX")
linha+=1
coluna = int(c_inicial)-1
print("\033["+str(linha)+";"+str(coluna)+"HXXX")
coluna = int(c_inicial)+14
print("\033["+str(linha)+";"+str(coluna)+"HXXX")
linha+=1
coluna = int(c_inicial)
print("\033["+str(linha)+";"+str(coluna)+"HX")
coluna+=15
print("\033["+str(linha)+";"+str(coluna)+"HX")

linha = int(l_inicial) + 15
print("\033["+str(linha)+";0H")


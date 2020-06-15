# encoding: utf-8 
# usando python 3
# Mensagem emoldurada - Implemente um programa que leia três linhas de mensagens de até 15
# caracteres cada uma e mostra-as na tela, emolduradas (retângulo ao redor) por algum caractere.
import os

linha1 = input("Escreva a linha 1 com até 15 caracteres: ")
linha2 = input("Escreva a linha 2 com até 15 caracteres: ")
linha3 = input("Escreva a linha 3 com até 15 caracteres: ")

os.system('clear') # para OSX 
print("\033[5;20H*******************")
print("\033[6;20H*                 *")
print("\033[7;20H*                 *")
print("\033[8;20H*                 *")
print("\033[9;20H*******************")

print("\033[6;22H"+linha1)
print("\033[7;22H"+linha2)
print("\033[8;22H"+linha3)

print("\033[10;0H")

# encoding: utf-8 
# usando python 3
# Múltipla escolha 1 - Elaborar uma questão de múltipla escolha, de uma disciplina 
# que esteja cursando ou um tema de interesse, com um enunciado e cinco alternativas, 
# sendo uma correta ou incorreta. Escrever um programa que mostra a questão na tela, pede a 
# resposta correta e informa ao usuário se este acertou ou errou.

import os

os.system('clear')

print("Em que ano foi o descobrimento do Brasil?")
print("")
print("a) 1500")
print("b) 1400")
print("c) 1300")
print("d) 1200")
print("")
resposta = input("Digite a escolha: ")
print("")
if resposta == "a":
	print("Parabéns você acertou!")
else:
	print("Ops...resposta errada")

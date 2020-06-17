# encoding: utf-8 
# usando python 3
# Múltipla escolha 2 - Enriqueça o programa acima da questão de múltipla escolha, 
# incluindo uma outra questão de outro tema. No início do programa, ofereça ao usuário a 
# escolha de qual questão quer responder.

import os

os.system('clear')

print("Escolha um dos temas: ")
print("")
print("a) História")
print("b) Geografia")
resposta = input("Digite a escolha: ")

if resposta == "a":
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
elif resposta == "b":
	print("Qual é o bioma predominante do estado de São Paulo")
	print("")
	print("a) Mata atlântica")
	print("b) Cerrado")
	print("c) Amazônico")
	print("d) Pantanal")
	print("")
	resposta = input("Digite a escolha: ")
	print("")
	if resposta == "b":
		print("Parabéns você acertou!")
	else:
		print("Ops...resposta errada")

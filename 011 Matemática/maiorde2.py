# encoding: utf-8 
# usando python 3
# Maior de 2 - Elaborar programa que lê dois números quaisquer e mostra na tela uma mensagem
# indicando qual é o maior, ou se são iguais.

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))

if num1 > num2:
	print(str(num1)+" é maior")
elif num2 > num1:
	print(str(num2)+" é maior")
else:
	print("Os números são iguais")
# encoding: utf-8 
# usando python 3
# Maior de 3 - Faça um programa que lê três números diferentes e mostra na tela uma 
# mensagem indicando qual é o maior.

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))
num3 = int(input("Digite o numero 3: "))

if num1 > num2:
	if num1 > num3:
		print(str(num1)+" é maior")
	elif num3 > num1:
		print(str(num3)+" é maior")
	else:
		print("Número 1 e 3 são iguais e maiores que o número 2")	
elif num2 > num1:
	if num2 > num3:
		print(str(num2)+" é maior")
	elif num3 > num2:
		print(str(num3)+" é maior")
	else:
		print("Número 2 e 3 são iguais e maiores que o número 1")	
elif num1 == num2:
	if num3 > num2: 
		print(str(num3)+" é maior")	
	elif num2 > num3:
		print(str(num2)+" é maior")	
	else: 
		print("Os números são iguais")

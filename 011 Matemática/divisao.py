# encoding: utf-8 
# usando python 3
# Divisão - Escrever um programa que lê dois números e efetua uma divisão, 
# mas somente se o divisor for diferente de zero; quando isto ocorrer,
# é mostrada uma mensagem de erro apropriada.

num1 = int(input("Digite o num1: "))
num2 = int(input("Digite o num2: "))

if num2 != 0:
	print(num1/num2)
else:
	print("Não é possivel dividir por 0")

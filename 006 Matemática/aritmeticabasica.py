# encoding: utf-8 
# usando python 3
# Aritmética básica - Implemente um programa que lê dois números quaisquer e informa sua
# soma, diferença, produto e quociente, formatados com 2 casas decimais.


num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

print("Soma = "+str(num1+num2))
print("Diferença = "+str(num1-num2))
print("Produto = "+str(num1*num2))
print("Quociente = "+"{:.2f}".format(num1/num2))
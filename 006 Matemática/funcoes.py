# encoding: utf-8 
# usando python 3
# Funções matemáticas - Elabore um programa que lê um número (suponha que será positivo) 
# e informa seu quadrado, raiz, logaritmo e exponencial, formatados com 4 casas decimais

import math

num = int(input("digite um numero positivo: "))
print("Quadrado = "+str(num**2))
print("Raiz = "+"{:.4f}".format(math.sqrt(num)))
print("{:.4f}".format(math.log(num)))
print("{:.4f}".format(math.exp(num)))

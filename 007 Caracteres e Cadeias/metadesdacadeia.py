# encoding: utf-8 
# usando python 3
# Metades de cadeia - Implemente um programa que lê uma cadeia de caracteres de tamanho até
# 255 e mostra na tela as metades da cadeia. [Dica: basear os cálculos no tamanho da cadeia]

frase = input("Digite uma frase com até 255 caracteres: ")

tamanho=len(frase)
metade = int(tamanho/2)
print(frase[0:metade])
print(frase[metade:tamanho-1])

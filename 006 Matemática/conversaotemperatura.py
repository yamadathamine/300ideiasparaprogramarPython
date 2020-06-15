# encoding: utf-8 
# usando python 3
# Conversão de temperatura - Um canal de notícias internacionais, a cabo, 
# previa temperatura máxima para Brasília de 85 graus Fahreneit. 
# Escrever um programa que lhe permita converter esta temperatura (e qualquer outra)
# para graus Celsius, sabendo que a relação entre elas é C =5/9 (F - 32).

F = int(input("Digite a temperatura em Fahreneit: "))
div = 5.0/9.0
celsius = (F-32) * div

print("{:.2f}".format(celsius))
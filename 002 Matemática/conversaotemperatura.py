# encoding: utf-8
# celsiusonversão de temperatura
# Faça um programa que calcula e mostra uma tabela de graus celsiuselsius/Fahrenheit de 1 a 10 
# [fórmula: celsius = (F-32) * 5/9]. Por enquanto (sem comandos de repetição), 
# você deverá escrever as instruções para calcular e mostrar cada resultado.

print("Fahrenheit -> Celsius")
F = 1
div = 5.0/9.0
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))
F = 2
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))
F = 3
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))
F = 4
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))
F = 5
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))
F = 6
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))
F = 7
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))
F = 8
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))
F = 9
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))
F = 10
celsius = (F-32) * div
print(str(F) + " -> " + "{:.2f}".format(celsius))



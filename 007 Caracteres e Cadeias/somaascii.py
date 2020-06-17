# encoding: utf-8 
# usando python 3
# Soma de códigos ASCII - Escreva um programa que lê uma cadeia de tamanho 3 e 
# mostra na tela a soma dos códigos ASCII dos caracteres da cadeia.

cadeia = input("Digite 3 caracteres: ")

soma = ord(cadeia[0])
soma += ord(cadeia[1])
soma += ord(cadeia[2])

print("Soma: "+str(soma))

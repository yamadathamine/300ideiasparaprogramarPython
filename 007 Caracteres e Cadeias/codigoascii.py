# encoding: utf-8 
# usando python 3
# Códigos ASCII - Escreva um programa que lê uma cadeia de caracteres qualquer, 
# e mostra na tela o código ASCII do primeiro e segundo caracteres da cadeia.

cadeia = input("Digite uma cadeia de caracteres: ")

caracter = ord(cadeia[0])
print(cadeia[0]+"-->"+str(caracter))
caracter = ord(cadeia[1])
print(cadeia[1]+"-->"+str(caracter))

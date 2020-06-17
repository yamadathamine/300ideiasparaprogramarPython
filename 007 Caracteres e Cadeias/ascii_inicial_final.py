# encoding: utf-8 
# usando python 3
# Códigos ASCII inicial e final - Elabore um programa que lê um nome de até 15 caracteres e
# mostra a inicial e seu código ASCII, e a última letra e seu código.

nome_completo = input("Digite o seu nome: ")

print(nome_completo[0]+" --> "+ str(ord(nome_completo[0])))
ultimo_caracter = len(nome_completo)-1
print(nome_completo[ultimo_caracter]+" --> "+ str(ord(nome_completo[ultimo_caracter])))
# encoding: utf-8 
# usando python 3
# Etiqueta - Escreva um programa que lê do teclado seu nome completo, 
# endereço, CEP e telefone, limpa a tela e mostra seu nome na primeira linha, 
# seu endereço na segunda, e o CEP e telefone na terceira.

import os

nome = input('Digite o seu nome completo: ')
endereco = input('Digite o seu endereço: ')
cep = input('Digite o CEP: ')
telefone = input('Digite o telefone: ')

os.system('clear')

print(nome)
print(endereco)
print("CEP:"cep+" Telefone:"+telefone)
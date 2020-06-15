# encoding: utf-8 
# usando python 3
# Média geométrica - 
# Elabore um programa que lê três valores e calcula a média geométrica dos números lidos 
# (divisão do produto pela quantidade de valores).


nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

media = (nota1*nota2*nota3)/3

print("Média = "+str(media))
# encoding: utf-8 
# usando python 3
# Média ponderada - 
# Implemente um programa que lê três valores e calcule a 
# média ponderada para pesos 1, 2 e 3, respectivamente 
# (multiplique cada nota pelo seu peso, some os produtos e divida o resultado pela soma dos pesos).

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

nota1 = nota1 * 1
nota2 = nota2 * 2
nota3 = nota3 * 3

media = (nota1+nota2+nota3)/6

print("Média = "+str(media))
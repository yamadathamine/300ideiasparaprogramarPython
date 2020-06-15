# encoding: utf-8 
# usando python 3
# Conversão cm/pol 1 - 
# Faça um programa que mostra 10 linhas de uma tabela de conversão centímetro/polegada, 
# a partir de um valor lido e variando de 10 em 10 centímetros 
# (uma polegada equivale a 2,54 centímetros).

num = int(input("Digite o valor em cm para converter para polegada: "))

pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
num += 10
pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
num += 10
pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
num += 10
pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
num += 10
pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
num += 10
pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
num += 10
pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
num += 10
pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
num += 10
pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
num += 10
pol = round(num/2.54,2)
print(str(num)+" cm -> "+str(pol)+" pol")
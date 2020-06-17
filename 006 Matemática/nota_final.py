# encoding: utf-8 
# usando python 3
# Notas do professor - Um professor avalia seus alunos através dos seguintes critérios:
# a) Duas notas de exercícios de 0 a 10, sem casas decimais, peso 1 e peso 2, 
# respectivamente, com peso de 20% na nota final.
# b) Uma nota de prova de 0 a 10, com uma casa decimal e peso de 80% na nota final.
# Elabore um programa que lê as notas de um aluno, calcula e mostra na tela sua nota final, 
# formatada com uma cada decimal e devidamente ponderada pelos pesos 
# (uma média ponderada é calculada somando-se os produtos de cada valor pelo seu peso e 
# dividindo-se a soma resultante pela soma dos pesos). Exemplo: Um aluno tirou 5 e 6 de exercícios 
# e 8,5 na prova. Sua nota de exercícios é (5*1 + 6*2)/3 = 5,667. 
# Sua nota final é (5,667*2 + 8,5*8)/10 = 7,9.

nota_exercicio1 = int(input("Nota exercicio 1: "))
nota_exercicio2 = int(input("Nota exercicio 2: "))
nota_prova = float(input("Nota prova: "))

media_exercicios = (nota_exercicio1 + (nota_exercicio2*2))/3
media_final = round((media_exercicios*2 + nota_prova*8)/10, 1)

print("Média: "+str(media_final))
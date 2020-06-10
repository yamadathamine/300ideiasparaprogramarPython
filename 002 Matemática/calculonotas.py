# encoding: utf-8
# Cálculo de notas - Um professor atribui pesos de 1 a 4 para as notas de quatro avaliações. 
# A nota é calculada por meio da média ponderada (N1 + N2*2 + N3*3 + N4*4)/10, 
# onde N1 é a nota da primeira avaliação, N2 a da segunda, etc..
# Um aluno tirou as seguintes notas: 8 - 7,5 - 10 - 9. 
# Faça um programa que calcula e mostra as notas e a média deste aluno, 
# sendo a média formatada com 1 casa decimal.

n1 = 8
n2 = 7.5
n3 = 10
n4 = 9
media = (n1 + n2*2 + n3*3 + n4*4)/10

print("Nota 1  "+str(n1))
print("Nota 2  "+str(n2))
print("Nota 3  "+str(n3))
print("Nota 4  "+str(n4))
print("-------------")
print("Média   "+"{:.1f}".format(media))
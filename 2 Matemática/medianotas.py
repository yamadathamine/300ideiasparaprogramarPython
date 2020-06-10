# encoding: utf-8
# Média de notas - Monte uma expressão matemática que calcula a média de suas notas (todas) 
# de um período anterior. Faça o cálculo através de um programa, mostrando na tela o resultado, 
# formatado com duas casas decimais e dentro de uma moldura (um retângulo feito com algum caractere).

media = (8.5 + 10 + 7 + 6.5 + 7.1 + 9.2)/6

print("***********************************")
print("*                                 *")
print("*               Média             *")
print("*                                 *")
print("*               "+"{:.2f}".format(media)+"              *")
print("*                                 *")
print("***********************************")
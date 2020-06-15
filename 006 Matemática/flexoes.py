# encoding: utf-8 
# usando python 3
# Quantidade de flexões 
# Um atleta faz flexões em série, com quantidades crescentes: 1 vez, depois 2 vezes, 
# 3, 4 e assim por diante. Ao final de uma sessão, ele quer saber rapidamente a 
# quantidade total de flexões que fez. Por exemplo, se ele fez 5 seqüências, 
# fez ao todo 15 flexões (5+4+3+2+1). 
# Implemente um programa que leia o número máximo e informe o total.


seq = int(input("digite a quantidade de sequências: "))

resultado = seq * (seq+1)/2

print("Total de flexões: "+str(resultado))




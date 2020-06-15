# encoding: utf-8 
# usando python 3
# Nota final - O critério de notas de uma faculdade consiste de uma nota de 0 a 10 em cada bimestre, 
# sendo a primeira nota peso 2 e a segunda peso 3. 
# Elabore um programa que lê as notas bimestrais e calcula a nota do semestre.

nota1 = int(input("Digite a nota do primeiro bimestre: "))
nota2 = int(input("Digite a nota do segundo bimestre: "))

media = ((nota1*2)+(nota2*3))/5

print(media)
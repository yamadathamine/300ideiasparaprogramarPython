# encoding: utf-8 
# usando python 3
# Aprovação 1 - Elaborar programa que lê uma disciplina e respectiva nota final, 
# múltipla de 0,5, e informa o que ocorreu. Se a nota for de 5 a 10, aprovado; se 4 ou 4,5, 
# recuperação e, caso contrário, reprovado.

nota_final = float(input("Digite a nota final: "))

if nota_final >= 5:
	print("Aprovado")
elif nota_final >= 4:
	print("Recuperação")
else:
	print("Reprovado")

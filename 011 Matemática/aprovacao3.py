# encoding: utf-8 
# usando python 3
# Aprovação 3 - Altere o programa acima para que leia também a quantidade de aulas 
# ministradas e a quantidade de faltas do aluno. Se o aluno não obteve 75% de freqüência, 
# ele está reprovado, independentemente da nota.

nota_final = float(input("Digite a nota final: "))
quantidade_aulas = int(input("Digite a quantidade de aulas: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

porc = faltas/quantidade_aulas * 100

if porc < 75:
	print("Reprovado")
else:
	if nota_final > 10 or nota_final < 0:
		print("Nota inválida")
	elif nota_final >= 5:
		print("Aprovado")
	elif nota_final >= 4:
		print("Recuperação")
	else:
		print("Reprovado")


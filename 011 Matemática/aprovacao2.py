# encoding: utf-8 
# usando python 3
# Aprovação 2 - Altere o programa acima para que, se a nota estiver fora da faixa válida, 
# seja emitida uma mensagem de erro.

nota_final = float(input("Digite a nota final: "))

if nota_final > 10 or nota_final < 0:
	print("Nota inválida")
elif nota_final >= 5:
	print("Aprovado")
elif nota_final >= 4:
	print("Recuperação")
else:
	print("Reprovado")

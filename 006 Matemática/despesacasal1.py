# encoding: utf-8 
# usando python 3
# Despesas de casal 1 - Um casal divide as despesas domésticas mensalmente. 
# Durante o mês cada um anota seus gastos e as contas que paga; no final eles dividem meio a meio. 
# O casal deseja um programa que facilite o acerto: eles digitariam os gastos de cada um, 
# e o programa mostraria quem deve a quem. Atualmente eles fazem o acerto manualmente, 
# na forma da seguinte tabela:

# ITEM 				| MARIDO	| ESPOSA	| TOTAL
# ----------------	|----------	|---------- |---------
# Despesas pagas	| 1278,60	| 875,30	| 2153,90
# % pago			| 59,36		| 40,64		| 100
# valor devido		| 1076,95	| 1076,95	| 2153,90
# Saldo				| 201,65	| -201,65	|
# 

# Portanto, os saldos devem ser iguais, e quem tiver o saldo negativo deve pagar o valor para o outro. 
# Faça um programa que leia os valores adequados e efetue os cálculos. 
# O total é a soma das despesas individuais; um percentual é o gasto individual dividido pelo total, 
# multiplicado por 100; o valor devido por cada um é o mesmo e igual à metade do total; finalmente, 
# cada saldo corresponde à metade da diferença entre o valor pago pela pessoa e o valor total.
import os

valor_marido = float(input("Digite o valor das despesas pagas pelo marido: "))
valor_esposa = float(input("Digite o valor das despesas pagas pela esposa: "))

total_despesas = round(valor_esposa + valor_marido,2)
porc_marido = round(valor_marido/total_despesas * 100, 2)
porc_esposa = 100 - porc_marido

valor_devido = round(total_despesas/2, 2)
saldo_marido = round(valor_marido - valor_devido,2)
saldo_esposa = round(valor_esposa - valor_devido,2)

os.system('clear')
print("\033[5;10HITEM")
print("\033[5;28HMARIDO")
print("\033[5;38HESPOSA")
print("\033[5;48HTOTAL")
print("\033[6;10H=============")
print("\033[6;28H=======")
print("\033[6;38H=======")
print("\033[6;48H=======")
print("\033[7;10HDespesas pagas")
print("\033[7;28H"+str(valor_marido))
print("\033[7;38H"+str(valor_esposa))
print("\033[7;48H"+str(total_despesas))
print("\033[8;10H% pago")
print("\033[8;28H"+str(porc_marido))
print("\033[8;38H"+str(porc_esposa))
print("\033[8;48H100")
print("\033[9;10HValor devido")
print("\033[9;28H"+str(valor_devido))
print("\033[9;38H"+str(valor_devido))
print("\033[9;48H"+str(total_despesas))
print("\033[10;10HSaldo")
print("\033[10;28H"+str(saldo_marido))
print("\033[10;38H"+str(saldo_esposa))









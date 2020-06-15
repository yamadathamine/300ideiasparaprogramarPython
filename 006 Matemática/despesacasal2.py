# encoding: utf-8 
# usando python 3
# Despesas de casal 2 - Altere o programa acima de forma que o marido arque com 
# 60% das despesas e a esposa com o restante.

import os

valor_marido = float(input("Digite o valor das despesas pagas pelo marido: "))
valor_esposa = float(input("Digite o valor das despesas pagas pela esposa: "))

total_despesas = round(valor_esposa + valor_marido,2)
porc_marido = round(valor_marido/total_despesas * 100, 2)
porc_esposa = 100 - porc_marido

valor_devido_marido = round(total_despesas*0.6, 2)
valor_devido_esposa = round(total_despesas*0.4, 2)
saldo_marido = round(valor_marido - valor_devido_marido,2)
saldo_esposa = round(valor_esposa - valor_devido_esposa,2)

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
print("\033[9;10HPorc a pagar")
print("\033[9;28H60")
print("\033[9;38H40")
print("\033[9;48H100")
print("\033[10;10HValor devido")
print("\033[10;28H"+str(valor_devido_marido))
print("\033[10;38H"+str(valor_devido_esposa))
print("\033[10;48H"+str(total_despesas))
print("\033[11;10HSaldo")
print("\033[11;28H"+str(saldo_marido))
print("\033[11;38H"+str(saldo_esposa))

# encoding: utf-8 
# usando python 3
# Despesas de casal 3 - Para o mesmo programa de rateio acima, suponha que o casal, 
# ao invés de dividir meio a meio as despesas, vai dividi-las proporcionalmente à renda 
# de cada um. Altere o programa de forma que este leia também a renda de cada um e use a 
# proporção das rendas para a divisão.

import os

valor_marido = float(input("Digite o valor das despesas pagas pelo marido: "))
valor_esposa = float(input("Digite o valor das despesas pagas pela esposa: "))
renda_marido = float(input("Digite a renda do marido: "))
renda_esposa = float(input("Digite a renda da esposa: "))

total_despesas = round(valor_esposa + valor_marido,2)
total_renda = round(renda_marido + renda_esposa, 2)

porc_esposa = round(renda_esposa/total_renda*100, 2)
porc_marido = round(100-porc_esposa, 2)

valor_devido_marido = round(total_despesas*porc_marido, 2)
valor_devido_esposa = round(total_despesas*porc_esposa, 2)
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
print("\033[8;10HRenda")
print("\033[8;28H"+str(renda_marido))
print("\033[8;38H"+str(renda_esposa))
print("\033[8;48H"+str(total_renda))
print("\033[9;10HPorc a pagar")
print("\033[9;28H"+str(porc_marido))
print("\033[9;38H"+str(porc_esposa))
print("\033[9;48H100")
print("\033[10;10HValor devido")
print("\033[10;28H"+str(valor_devido_marido))
print("\033[10;38H"+str(valor_devido_esposa))
print("\033[10;48H"+str(total_despesas))
print("\033[11;10HSaldo")
print("\033[11;28H"+str(saldo_marido))
print("\033[11;38H"+str(saldo_esposa))

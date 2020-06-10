# encoding: utf-8
#Imposto - Um imposto é calculado com base na seguinte tabela:
# Até	     1.200,00				isento
# de         1.201,00 a 5.000,00 	10%
# de 	     5.001,00 a 10.000,00 	15%
# acima de   10.000,00 				20%

# Implemente um programa que calcule os impostos a pagar para um valor em cada faixa. 
# Para cada um, mostre uma mensagem que identifique na tela a que se refere cada valor.

print("Para um salário de	| Imposto a pagar")
print(" 1.000,00         	| isento")
salario = 3000.00
imposto = salario * 0.1
print(" 3.000,00         	| "+"{:.2f}".format(imposto))
salario = 7000.00
imposto = salario * 0.15
print(" 7.000,00        	| "+"{:.2f}".format(imposto))
salario = 15000.00
imposto = salario * 0.2
print("15.000,00        	| "+"{:.2f}".format(imposto))
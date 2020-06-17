# encoding: utf-8 
# usando python 3
# Conta telefônica - Uma conta telefônica é composta dos seguintes custos:
# assinatura: R$ 21,40
# impulsos: R$ 0,03 por impulso que exceder a 90 
# interurbanos
# chamadas p/ celular: R$0,40 por impulso
# Elabore um programa que lê os impulsos excedentes, valor de interurbanos e 
# quantidade de chamadas para celular e calcula o valor da conta. 
# Ao definir a tela, imagine que está fazendo um produto para ser avaliado por um cliente, 
# juntamente com o de concorrentes, para uma eventual compra.
import os

impulsos_total = int(input("Digite a quantidade total de impulsos: "))
valor_interurbano = float(input("Digite o valor de interurbanos: "))
impulsos_celular = int(input("Digite a quantidade de impulsos para celular: "))
impulsos_a_mais = impulsos_total - 90
valor_impulsos = impulsos_a_mais * 0.03
valor_assinatura = 21.40
valor_celular =impulsos_celular * 0.40

valor_total = valor_impulsos + valor_interurbano + valor_celular + valor_assinatura

os.system('clear') # para OSX 
print(" __________________________________________________")
print("|                                                  |")
print("|                Conta telefônica                  |")
print("|__________________________________________________|")
print("")
print(" * Valor assinatura_______________________R$ 21.40")
print(" * Valor impulsos_________________________R$  "+"{:.2f}".format(valor_impulsos))
print(" *** Impulsos total:                 "+str(impulsos_total))
print(" *** Impulsos incluidos na franquia: 90")
print(" *** Impulsos a cobrar:              "+str(impulsos_a_mais))
print(" *** Valor por impulsos a cobrar:    R$0.03")
print(" * Valor interurbano______________________R$ "+"{:.2f}".format(valor_interurbano))
print(" * Valor celular__________________________R$  "+"{:.2f}".format(valor_celular))
print(" *** Impulsos total:                 "+str(impulsos_celular))
print(" *** Valor por impulsos celular:     R$0.40")
print(" Total____________________________________R$ "+"{:.2f}".format(valor_total))







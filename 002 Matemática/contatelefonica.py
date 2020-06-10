# encoding: utf-8
# Conta telefônica - Uma conta telefônica é composta dos seguintes custos:
# assinatura: R$ 17,90
# impulsos: R$ 0,04 por impulso que exceder a 90
# chamadas p/ celular: R$0,20 por impulso
# Monte a fórmula para calcular o valor da conta para 254 impulsos, 
# R$34,29 de interurbanos e 23 chamadas para celular. 
# Elabore um programa que mostra os custos, calcula e mostra o valor total.
import os

impulsos_a_mais = 254 - 90
valor_impulsos = impulsos_a_mais * 0.04
valor_assinatura = 17.90
valor_celular = 23 * 0.20
valor_interurbano = 34.29
valor_total = valor_impulsos + valor_interurbano + valor_celular + valor_assinatura

os.system('clear') # para OSX 
print(" ____________________________________")
print("|                                    |")
print("|         Conta telefônica           |")
print("|____________________________________|")
print("")
print(" * Valor assinatura_______________________R$ 17.90")
print(" * Valor impulsos_________________________R$  "+"{:.2f}".format(valor_impulsos))
print(" *** Impulsos total:                 254")
print(" *** Impulsos incluidos na franquia: 90")
print(" *** Impulsos a cobrar:              "+str(impulsos_a_mais))
print(" *** Valor por impulsos a cobrar:    R$0.04")
print(" * Valor interurbano______________________R$ 34.29")
print(" * Valor celular__________________________R$  "+"{:.2f}".format(valor_celular))
print(" *** Impulsos total:                 23")
print(" *** Valor por impulsos celular:     R$0.20")
print(" Total____________________________________R$ "+"{:.2f}".format(valor_total))

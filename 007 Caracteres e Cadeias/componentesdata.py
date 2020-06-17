# encoding: utf-8 
# usando python 3
# Componentes de data - Escrever um programa que lê uma data no formato ‘dd/mm/aa’ e 
# mostra dia, mês e ano separados.

data = input("Digite uma data no formato(dd/mm/aa): ")

componentes = data.split("/")

print("Dia: "+componentes[0])
print("Mês: "+componentes[1])
print("Ano: "+componentes[2])
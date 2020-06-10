# encoding: utf-8
# Tempo dedicado - Uma pessoa com pouco tempo disponível lê um livro por 5 minutos a cada dia, 
# 6 dias por semana. Monte a fórmula e escreva um programa que calcula e mostra na tela quanto tempo, 
# em horas, a pessoa terá dedicado ao livro ao final de um ano.

semanas_ano = 52
total_dias = semanas_ano * 6
total_minutos = total_dias * 5
horas_final = total_minutos // 60
minutos_final = total_minutos%60

print("Considerando que um ano tem 52 semanas")
print("e a pessoa lê 6 dias por semana ao final de um ano ela terá dedicado: ")
print(str(horas_final)+" horas e "+str(minutos_final)+" minutos")
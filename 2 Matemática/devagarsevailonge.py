# encoding: utf-8
# Devagar se vai ao longe
# Vou e volto diariamente a pé para o trabalho, que dista aproximadamente 800 m de minha casa. 
# Supondo que trabalho 5 dias por semana, 45 semanas por ano, 
# "bole" a operação matemática que deve ser efetuada para calcular quantos quilômetros, 
# aproximadamente, terei andado ao final de um ano. 
# Elabore um programa que faça as contas e mostre o resultado na tela.

distancia = 800
total_metros = distancia * 2 * 5 * 45
quilometros = total_metros//1000

print("Aproximadamente "+str(quilometros)+" km")
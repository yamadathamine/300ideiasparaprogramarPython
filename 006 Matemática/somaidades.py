# encoding: utf-8 
# usando python 3
# Soma das idades - Uma criança quer saber qual é a soma de todas as idades que ela já teve. 
# Elaborar programa que lê uma idade qualquer e responde rapidamente a essa pergunta 
# [fórmula para calcular a soma dos N primeiros números inteiros: N (N+1)/2].

idade = int(input("digite a idade: "))

resultado = idade * (idade+1)/2

print(resultado)
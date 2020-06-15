# encoding: utf-8 
# usando python 3
# Adivinha - Escrever um programa que “adivinha” o número pensado por uma pessoa 
# (Pense um número (pausa), multiplique por 2 (pausa), some 6 ao resultado (pausa), 
# divida o resultado por 2, quanto deu? (informe o resultado), você pensou o número tal). 
# [Dica: problemas desse tipo dão origem a uma expressão aritmética, e você pode alterar as 
# operações à vontade, desde que a expressão resultante admita uma inversa. 
# Normalmente estruturamos o problema de forma que a expressão permita uma simplificação que 
# facilite os cálculos. Para a seqüência proposta, a expressão é (sendo n o número pensado e R o 
# resultado): (n*2+6)/2 = R, donde n = (R*2-6)/2 = R - 3. Ou seja, basta subtrair 3 do 
# resultado fornecido pela pessoa para "adivinhar" o número].


import os

os.system('clear')

input("Pense em um número!")
input("Multiplique por 2")
input("Some 6 ao resultado")
input("Divida o resultado por 2")
resultado = int(input("Digite o valor que deu: "))

print("Você pensou no número "+str(resultado-3)+"!!")
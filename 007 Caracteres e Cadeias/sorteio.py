# encoding: utf-8 
# usando python 3
# Sorteio da LBV - A LBV fez um sorteio cujos bilhetes continham números de 6 dígitos. 
# O sorteio foi baseado nos dois primeiros prêmios da loteria federal, 
# sendo o número sorteado formado pelos três últimos dígitos do primeiro e do segundo prêmio. 
# Por exemplo, se o primeiro prêmio fosse 34.582 e o segundo 54.098, o número da LBV seria 582.098. 
# Escreva um programa que lê os dois prêmios e retorna o número sorteado.

primeiro_premio = input("Digite o primeiro prêmio: ")
segundo_premio = input("Digite o segundo prêmio: ")

sorteado = primeiro_premio.split(".")[1]
sorteado += "."
sorteado += segundo_premio.split(".")[1]

print("Número sorteado: "+sorteado)
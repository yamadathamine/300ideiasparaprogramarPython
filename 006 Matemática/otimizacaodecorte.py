# encoding: utf-8 
# usando python 3
# Otimização de corte - Reescreva o programa 1.2.5 (corte de tábuas) 
# para que leia o tamanho de cada tábua e o comprimento de cada pedaço, 
# e calcule a quantidade de pedaços e a sobra para cada tipo de tábua.
# Otimização de corte - Um marceneiro, para fazer um trabalho, precisa cortar vários 
# pedaços de madeira de 45 cm cada um. Ele pode comprar tábuas de 3, 4 ou 5 metros. 
# Usando os operadores div e mod, faça um programa que calcule a quantidade de pedaços 
# e a sobra para cada tipo de tábua, permitindo assim uma melhor escolha do marceneiro.

comprimento = int(input("digite o comprimento desejado (em cm): "))
tamanho1 = int(input("digite o tamanho da tabua 1 (em cm): "))
tamanho2 = int(input("digite o tamanho da tabua 2 (em cm): "))
tamanho3 = int(input("digite o tamanho da tabua 3 (em cm): "))
qtd_pedacos = tamanho1//comprimento
qtd_sobra = tamanho1%comprimento
print(" Tamanho | Pedaços |	Sobra")
print(str(tamanho1)+"cm | "+str(qtd_pedacos)+" | " + str(qtd_sobra))
qtd_pedacos = tamanho2//comprimento
qtd_sobra = tamanho2%comprimento
print(str(tamanho2)+"cm | "+str(qtd_pedacos)+" | " + str(qtd_sobra))
qtd_pedacos = tamanho3//comprimento
qtd_sobra = tamanho3%comprimento
print(str(tamanho3)+"cm | "+str(qtd_pedacos)+" | " + str(qtd_sobra))

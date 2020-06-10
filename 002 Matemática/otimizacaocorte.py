# encoding: utf-8
# Otimização de corte - Um marceneiro, para fazer um trabalho, precisa cortar vários 
# pedaços de madeira de 45 cm cada um. Ele pode comprar tábuas de 3, 4 ou 5 metros. 
# Usando os operadores div e mod, faça um programa que calcule a quantidade de pedaços 
# e a sobra para cada tipo de tábua, permitindo assim uma melhor escolha do marceneiro.

qtd_pedacos = (3*100)//45
qtd_sobra = (3*100)%45
print(" Tamanho | Pedaços |	Sobra")
print("3 metros | "+str(qtd_pedacos)+" | " + str(qtd_sobra))
qtd_pedacos = (4*100)//45
qtd_sobra = (4*100)%45
print("4 metros | "+str(qtd_pedacos)+" | " + str(qtd_sobra))
qtd_pedacos = (5*100)//45
qtd_sobra = (5*100)%45
print("5 metros | "+str(qtd_pedacos)+" | " + str(qtd_sobra))
# encoding: utf-8 
# usando python 3
# Comprimento de fio - 
# Altere o programa do eletricista (1.2.10 ) para que as medidas sejam lidas do teclado.


import math

largura = float(input("largura: "))
comprimento = float(input("comprimento: "))

print("{:.3f}".format(math.sqrt(largura**2 + comprimento**2)))
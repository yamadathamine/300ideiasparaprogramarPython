# encoding: utf-8
# Comprimento de fio - Um eletricista precisa comprar fio
# que irá passar, pelo telhado, por toda a diagonal de uma casa de
# formato retangular. Como ele não tem condições de medir a
# diagonal com precisão (ou talvez não queira...), a solução
# alternativa que ele encontrou foi medir os lados da casa, sabendo
# que a diagonal pode ser calculada com base nos lados pelo
# Teorema de Pitágoras (a2 = b2 + c2). 
# Considerando que a casa mede 11,5 x 6,3 metros, 
# faça um programa que calcule a quantidade mínima necessária de fio a ser comprada, 
# com precisão até centímetros.
import math

print("{:.3f}".format(math.sqrt(11.5**2 + 6.3**2)))
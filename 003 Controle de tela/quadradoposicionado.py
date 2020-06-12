# encoding: utf-8
# Quadrado posicionado
# Refaça o programa que desenha o "quadrado" no alto da tela,
# desta vez desenhando-o com o canto superior esquerdo na linha 7, coluna 20.

import os

os.system('clear') # para OSX 
print("\033[7;20H##########")
print("\033[8;20H#        #")
print("\033[9;20H#        #")
print("\033[10;20H#        #")
print("\033[11;20H##########")
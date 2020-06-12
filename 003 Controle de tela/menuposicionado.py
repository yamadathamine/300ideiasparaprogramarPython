# encoding: utf-8 
# usando python 3
# Menu posicionado
# Elabore um programa que mostre um menu centralizado na tela, 
# e espera uma tecla ser pressionada para terminar.
# Use comandos de posicionamento do cursor para facilitar.

import os

os.system('clear') # para OSX 
print("\033[15;40H Menu relatórios")
print("\033[17;40H 1 - Por nome")
print("\033[18;40H 2 - Por código")
print("\033[19;40H 3 - Por data")
print("\033[20;40H 4 - Fim")

teste=input("\033[22;30HOpção: ")
# encoding: utf-8 
# usando python 3
# Triângulo com iniciais - Escrever um programa que desenha um triângulo, 
# aproximadamente centralizado, na tela (que em modo texto normal tem 80 colunas por 25 linhas), 
# tendo dentro as iniciais do seu nome. Faça o programa limpar a tela no início e esperar 
# uma tecla antes de terminar.

import os

os.system('clear') # para OSX 

print("\033[12;40H*")
print("\033[13;39H* *")
print("\033[14;38H*   *")
print("\033[15;37H*     *")
print("\033[16;36H*  TTY  *")
print("\033[17;35H*         *")
print("\033[18;34H*           *")
print("\033[19;33H***************")
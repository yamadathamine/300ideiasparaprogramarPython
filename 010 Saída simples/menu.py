# encoding: utf-8 
# usando python 3
# Menu principal - Faça um programa de menu que mostra na tela, sob o título de "Menu Principal", 
# três opções: "1 - Fim", "2 - Cadastro" e "3 - Consulta", lê do teclado a opção desejada pelo 
# usuário e mostra uma mensagem confirmando a opção escolhida ou uma mensagem de erro, se a opção 
# for inválida.


import os

os.system('clear')

print("\033[10;10H Menu principal")
print("\033[11;10H 1 - Fim")
print("\033[12;10H 2 - Cadastro")
print("\033[13;10H 3 - Consulta")
opcao=int(input("\033[16;10HOpção: "))

if opcao == 1:
	print("Fim do programa.")
elif opcao == 2:
	print("Cadastro escolhido.")
elif opcao == 3:
	print("Consulta escolhido.")
else:
	print("Opção inválida.")
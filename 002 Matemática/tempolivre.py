# encoding: utf-8
# Tempo livre - Um estudante muito metódico estava matriculado em 6 disciplinas, 
# e dispunha de 1 hora e 40 minutos para estudar. 
# Sua intenção era dividir o tempo disponível igualmente para as 6 
# disciplinas, e descansar livremente o tempo restante. 
# Faça um programa que calcule o tempo que ele deve dedicar para cada disciplina e o tempo livre. 
# [Dica: use os operadores div e mod]

total_minutos = 60+40
tempo_disciplina = total_minutos//6
tempo_descanso = total_minutos%6
print("Tempo de estudo para cada disciplina = "+str(tempo_disciplina)+" minutos")
print("Tempo de descanso = "+str(tempo_descanso)+" minutos")
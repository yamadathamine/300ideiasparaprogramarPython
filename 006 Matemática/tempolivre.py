# encoding: utf-8 
# usando python 3
# Tempo livre - Reescreva o programa 1.2.4 (o estudante metódico) de forma 
# que trate qualquer disciplina e qualquer quantidade de tempo livre. 
# Assim, o estudante entra com esses valores e o programa efetua os cálculos necessários.

disciplinas = int(input("disciplinas: "))
tempo_total = int(input("tempo total (coloque em minutos): "))

tempo_disciplina = tempo_total//disciplinas
tempo_descanso = tempo_total%disciplinas
print("Tempo de estudo para cada disciplina = "+str(tempo_disciplina)+" minutos")
print("Tempo de descanso = "+str(tempo_descanso)+" minutos")
#O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunos = []

for i in range(1, 5):
    nomes = str(input(f"Digite o nome do {i}º aluno: "))
    nome_maiusc = nomes.capitalize()
    alunos.append(nome_maiusc)
print("")
print(f"Os alunos são: {alunos}\n")

shuffle(alunos)

print(f"A ordem sorteada foi: {alunos}\n")


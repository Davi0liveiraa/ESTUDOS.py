#Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

alunos=  []
for i in range(1,5):
    nomes = str(input(f"Nome do {i}º aluno: "))
    alunos.append(nomes)

sorteado = random.choice(alunos)
print(f" O aluno escolhido foi: {sorteado}")
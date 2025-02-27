'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
num_sorteado = randint(1, 5)
num = int(input("Digite um número de 1 à 5:\n"))
if num == num_sorteado:
    print("Você venceu!\n")
else:
    print(f"Você perdeu! O número era {num_sorteado}\n")


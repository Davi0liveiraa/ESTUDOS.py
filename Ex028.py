'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from time import sleep
from random import randint
num_sorteado = randint(0, 5)
print("\n","-=-"*20)
print("   Vou pensar em um número de 0 à 5. Tente adivinhar...")
print("-=-"*20,"\n")
num = int(input("Em que número pensei?"))
print("PROCESSANDO...")
sleep(3)
if num == num_sorteado:
    print("\nPARABÉNS! Você conseguiu me vencer!")
else:
    print(f"\nGANHEI! Eu pensei no número {num_sorteado}, e não no {num}")


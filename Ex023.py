'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados em unidade, dezena, centena e milhar.'''

numero = int(input("Digite o núemero: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
unidade = u
dezena = d
centena = c
milhar = m

print(f"\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}\n")
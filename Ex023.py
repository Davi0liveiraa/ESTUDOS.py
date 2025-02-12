'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados em unidade, dezena, centena e milhar.'''

numero = str(input("Digite o núemero: "))
lista = numero.split()
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

print(f"\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}\n")
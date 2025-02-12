'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input("Digite seu nome completo: "))
print(f"Primeiro nome: {nome.split()[0]}")
print(f"Segundo nome: {nome.split()[1]}")
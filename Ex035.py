'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

r1 = int(input("Digite o cumprimento da reta 1: \n"))
r2 = int(input("Digite o cumprimento da reta 2: \n"))
r3 = int(input("Digite o cumprimento da reta 3: \n"))

if (r1 + r2 > r3) or (r2+r3 > r1) or (r1+r3 > r2):
    print("Medidas capazes de formar um triângulo.\n")
else:
    print("Medidas incapazes de formar um triângulo.\n")
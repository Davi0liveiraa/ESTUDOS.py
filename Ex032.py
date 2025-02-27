'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

ano = int(input("Digite um ano qualquer: "))
dias = int(input("Digite a quantidade de dias desse ano: "))

if dias != 365 and dias != 366:
    print("Ano inválido.\n") 
elif dias == 365:
    print("Ano normal.\n")
elif dias == 366:
    print("Ano bissexto!\n")
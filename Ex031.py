'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,5O por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''

km = float(input("Qual a distância da viagem em Km?\n"))
if km <= 200:
    preco = 0.50*km
    print(f"Valor da viagem: R${preco:.2f}\n")
else:
    preco = 0.45*km
    print(f"Valor da viagem: R${preco:.2f}\n")

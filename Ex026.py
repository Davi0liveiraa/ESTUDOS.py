'''Crie um programa que leia uma frase pelo teclado e mostre: 

-Quantas vezes aparece a letra "A"

-Em qual posição ela aparece a primeira vez

-Em que posição ela aparece a ultima vez'''

frase = str(input("Digite uma frase: ").upper())
qtd_a = frase.count('A')
print(qtd_a)
print(frase.find('A'))
print(frase.rfind('A'))
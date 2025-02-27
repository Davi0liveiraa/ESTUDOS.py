'''Crie um programa que leia uma frase pelo teclado e mostre: 

-Quantas vezes aparece a letra "A"

-Em qual posição ela aparece a primeira vez

-Em que posição ela aparece a ultima vez'''

frase = str(input("Digite uma frase: ").upper().strip())
qtd_a = frase.count('A')
print(qtd_a)
print(frase.find('A')+1)
print(frase.rfind('A')+1)
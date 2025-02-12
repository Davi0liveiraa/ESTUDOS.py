'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
-O nome com todas as letras maíusculas. 
-O nome com todas minúsculas. 
-Quantas letras ao todo.(Sem considerar espaços.) 
-Quantas letras tem o primeiro nome.'''


nome = str(input("Digite seu nome completo: "))
nome_maiusc = nome.upper()
print("")
print(nome_maiusc)
nome_minusc = nome.lower()
print(nome_minusc)
nome_sem_espaço = ''.join(nome.split())
quantidade_letras = len(nome_sem_espaço)
print(quantidade_letras)
primeiro_nome = nome.split()[0]
print(primeiro_nome)
print("")
'''
Crie um programa que leia o nome completo de uma pessoa e mostra:
a) O nome com todas as letras maiúsculas e minúsculas.
b) Quantas letras ao todo (sem considerar espaços).
c) Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip()
nome_sem_espacos = nome.split()

print(nome.upper())
print(nome.lower())
print(f"Total de letras: {len(nome) - nome.count(' ')}")
print(f'Total de letras do primeiro nome: {len(nome_sem_espacos[0])}')
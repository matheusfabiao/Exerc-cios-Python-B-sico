# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome: ')).strip().upper().split()

if 'SILVA' in nome:
    print('Você tem "SILVA" no nome')
else:
    print('Você não tem "SILVA" no nome')
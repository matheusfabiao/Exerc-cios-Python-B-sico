'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex:
primeiro: Ana
último: Souza
'''

nome = str(input('Digite o nome e sobrenome: ')).strip().title().split()

print('primeiro:', nome[0])
print('último:', nome[-1])
# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    print('Número par!')
elif num % 2 != 0:
    print('Número ímpar!')
else:
    print('Algo deu errado!')
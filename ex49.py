# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Enunciado do DESAFIO 009:

# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

print('-'*15)
num = int(input('Digite um número inteiro: '))

for fator in range(1, 11):
    print(f'{num} x {fator} = {num * fator}')
    fator += 1
print('-'*15)
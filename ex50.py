# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0

for num in range(1, 7):
    num = int(input(f'Digite o {num}º número inteiro: '))
    if num % 2 == 0:
        soma += num
        contador += 1

print(f'Você informou um total de {contador} de números pares cuja a soma deles é igual a {soma}')
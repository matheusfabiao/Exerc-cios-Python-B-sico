# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

lista = list()
contador = 1
while contador <= 3:
    num = float(input('Digite um número: '))
    lista.append(num)
    contador += 1

print(f'O maior número foi {max(lista)}')
print(f'O menor número foi {min(lista)}')
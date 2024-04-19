# Crie um programa que leia um número Real qualquer pelo teclado a mostre na tela a sua porção Inteira.

num = float(input('Digite um número real: '))

# MÉTODO 1 - IMPORT MATH
from math import trunc

print(f'A porção inteira de {num} é {trunc(num)}')

# MÉTODO 2 - OPERAÇÃO DE CASTING
print(f'A porção inteira de {num} é {int(num)}')
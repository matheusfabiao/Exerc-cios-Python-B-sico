# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite a medida do ângulo em graus: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Seno de {angulo}°: {seno:.2f}')
print(f'cosseno de {angulo}°: {cosseno:.2f}')
print(f'tangente de {angulo}°: {tangente:.2f}')
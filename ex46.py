# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from datetime import date
from time import sleep

print('INCIANDO A CONTAGEM REGRESSIVA...')
sleep(2)

for seg in range(10, -1, -1):
    print(seg)
    sleep(1)

print('FELIZ ANO NOVO!!!!')
print(f'ESTAMOS NO ANO DE {date.today().year}!')
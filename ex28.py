# Escreva um programa que faça o computador "pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-='*20)
print('Vou pensar em um número de 0 a 5. Tente advinhar...')
sleep(3) # Causa um "efeito" de processamento
print('PROCESSANDO...')
computador = randint(0, 5) # Fazendo o computador "pensar"
sleep(3)
print('Em qual número eu pensei??')
print('-='*20)

usuario = int(input('Diga seu palpite: ')) # Palpite do usuário
sleep(1)
print('AGUARDE...')
sleep(2)

# Define a resposta ao usuário baseado em seu palpite
if usuario == computador:
    print('Você acertou! O número escolhido foi:', computador)
else:
    print('Você errou! O número escolhido foi:', computador)
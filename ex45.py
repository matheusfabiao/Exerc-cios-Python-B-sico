# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

jogador = str(input('Faça sua jogada: ')).strip().lower()
computador = choice(jogadas)

print('Jogada do computador:', computador)

if jogador == 'pedra':
    if computador == 'pedra':
        print('O jogo acabou em EMPATE!')
    elif computador == 'papel':
        print('Você PERDEU!')
    elif computador == 'tesoura':
        print('Você GANHOU!')
    else:
        print('Algo deu errado!')
elif jogador == 'papel':
    if computador == 'pedra':
        print('Você GANHOU!')
    elif computador == 'papel':
        print('O jogo acabou em EMPATE!')
    elif computador == 'tesoura':
        print('Você PERDEU!')
    else:
        print('Algo deu errado!')
elif jogador == 'tesoura':
    if computador == 'pedra':
        print('Você PERDEU!')
    elif computador == 'papel':
        print('Você GANHOU!')
    elif computador == 'tesoura':
        print('O jogo acabou em EMPATE!')
    else:
        print('Algo deu errado!')
else:
    print('ALGO DEU ERRADO!')
print('FIM DO JOGO!')
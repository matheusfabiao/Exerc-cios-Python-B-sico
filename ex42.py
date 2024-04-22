# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

# ENUNCIADO DO DESAFIO 035:

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Regra: a soma de dois lados é sempre menor que o terceiro lado.

reta_1 = float(input('Digite o valora da reta 1: '))
reta_2 = float(input('Digite o valora da reta 2: '))
reta_3 = float(input('Digite o valora da reta 3: '))

# Primeiro verifica se as retas podem formar um triângulo
if (reta_1 < reta_2 + reta_3) and (reta_2 < reta_1 + reta_3) and (reta_3 < reta_1 + reta_2):
    # Se puderem formar, adiciona mais um bloco de condição para classificação do triângulo
    if reta_1 == reta_2 == reta_3:
        print('Triângulo equilátero.')
    elif (reta_1 == reta_2) or (reta_1 == reta_3) or (reta_2 == reta_3):
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')
else:
    print('As retas não podem formar um triângulo!')

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.
# Regra: a soma de dois lados é sempre menor que o terceiro lado.

reta_1 = float(input('Digite o valora da reta 1: '))
reta_2 = float(input('Digite o valora da reta 2: '))
reta_3 = float(input('Digite o valora da reta 3: '))

if (reta_1 < reta_2 + reta_3) and (reta_2 < reta_1 + reta_3) and (reta_3 < reta_1 + reta_2):
    print('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')
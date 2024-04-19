# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule a mostre o comprimento da hipotenusa. Fórmula c2=a2+b2

co = float(input('Digite o comprimento do C.O: '))
ca = float(input('Digite o comprimento do C.A: '))

hp = (co**2 + ca**2) ** (1/2)

print(f'Valor da hipotenusa: {hp:.2f}')
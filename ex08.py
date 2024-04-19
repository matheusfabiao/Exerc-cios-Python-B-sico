# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# km hm dam m dm cm mm

metros = float(input('Digite um valor: '))

cent = metros * 100
mili = metros * 1000

print(f'O valor de {metros}m em centímetros é {cent:.0f}cm')
print(f'O valor de {metros}m em milímetros é {mili:.0f}mm')
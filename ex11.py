# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = largura * altura
litros = area / 2

print(f'São necessários {litros:.2f}L de tinta para pintar uma área de {area:.2f}m²')
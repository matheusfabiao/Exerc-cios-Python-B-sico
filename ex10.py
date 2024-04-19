# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$5.24 (abril de 2024)

real = float(input('Digite o valor em R$: '))

dolar = real / 5.24

print(f'Você pode comprar US${dolar:.2f}')
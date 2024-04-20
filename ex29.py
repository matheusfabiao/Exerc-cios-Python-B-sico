# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade do veículo: '))
limite = 80

if velocidade <= limite:
    print('Veículo não multado. Prossiga...')
else:
    preco = (velocidade - limite) * 7
    print(f'Veículo foi multado em R${preco:.2f}')
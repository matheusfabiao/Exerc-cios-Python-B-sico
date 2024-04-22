# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do produto em R$: '))
print()
print('-='*23)
print('[1] À vista dinheiro/cheque: 10% de desconto')
print('[2] À vista no cartão: 5% de desconto')
print('[3] Em até 2x no cartão: preço normal')
print('[4] 3x ou mais no cartão: 20% de juros')
print('-='*23)
print()
opcao = int(input('Selecione a forma de pagamento: '))

if opcao == 1:
    novo_preco = preco - (preco * 10/100)
elif opcao == 2:
    novo_preco = preco - (preco * 5/100)
elif opcao == 3:
    novo_preco = preco / 2
elif opcao == 4:
    total = preco + (preco * 20/100)
    total_parcelas = int(input('Digite a qntd de parcelas: '))
    novo_preco = total / total_parcelas
else:
    print('Digite uma opção válida!')
    
print(f'Sua compra vai custar: R${novo_preco:.2f}')
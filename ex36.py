# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Digite quantas prestações: '))

prestacao_mensal = casa / (anos*12)

if prestacao_mensal <= (salario * 30/100):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo não aprovado!')
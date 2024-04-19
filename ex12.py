# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Digite o preço: '))

novo_preco = preco - (preco * 5/100)

print(f'O valor de R${preco:.2f} com 5% de desconto fica R${novo_preco:.2f}')
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor: '))

novo_salario = salario + (salario * 15/100)

print(f'O valor de R${salario:.2f} com 15% de aumento fica R${novo_salario:.2f}')
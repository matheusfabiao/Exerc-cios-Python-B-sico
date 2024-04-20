# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário em R$: '))

if salario > 1250:
    aumento = salario + (salario * 10/100)
    print(f'O salário ficará {aumento} com o aumento de 10%')
else:
    aumento = salario + (salario * 15/100)
    print(f'O salário ficará {aumento:.2f} com o aumento de 15%')
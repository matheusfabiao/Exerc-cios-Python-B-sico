# Faça um programa que calcule a soma entre todos os números ímpares que SÃO múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 # realiza a soma pedida acima
contador = 0 # conta o total de números que atendem os requisitos

for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num # soma = soma + num
        contador += 1 # contador = contador + 1

print(f'A soma dos {contador} números ímpares e múltiplos de 3 é igual a {soma}')
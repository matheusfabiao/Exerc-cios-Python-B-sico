'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número inteiro de 0 a 9999: 1834
Retorno esperado -> Unidade: 4  Dezena 3    Centena: 8  Milhar: 1
'''

num = int(input('Digite um número inteiro de 0 a 9999: '))

# MINHA SOLUÇÃO (AVANÇADA)
if num in range(0, 10000):
    num = str(num).strip()
    if len(num) == 4:
        print(f'unidade: {num[-1]}  dezena: {num[-2]}  centena: {num[-3]}  milhar: {num[-4]}')
    elif len(num) == 3:
        print(f'unidade: {num[-1]}  dezena: {num[-2]}  centena: {num[-3]}')
    elif len(num) == 2:
        print(f'unidade: {num[-1]}  dezena: {num[-2]}')
    elif len(num) == 1:
        print(f'unidade: {num[-1]}')
else:
    print('ERRO: Número fora de alcance!')
    
'''
# SOLUÇÃO DO GUANABARA (MATEMÁTICA):
num = int(input('Informe um número: '))
u = num // 1 % 10  # Divisão inteira por 1 e resto da divisão por 10
d = num // 10 % 10  # Divisão inteira por 10 e resto da divisão por 10
c = num // 100 % 10  # Divisão inteira por 100 e resto da divisão por 10
m = num // 1000 % 10  # Divisão inteira por 1 e resto da divisão por 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
'''

'''
# SOLUÇÃO DO CHAT (SIMPLES)
num = int(input('Digite um numero: '))
n = num + 10000
nn = str(n)
print(f'A unidade é: {nn[-1]}')
print(f'A dezena é: {nn[-2]}')
print(f'A centena é: {nn[-3]}')
print(f'O milhar é: {nn[1]}')
'''
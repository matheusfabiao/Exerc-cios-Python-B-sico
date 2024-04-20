# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1) para binário
# 2) para octal
# 3) para hexadecimal

print('-='*15)
num = int(input('Digite um número inteiro: '))

print('-='*15)
print()
print('Menu de opções:')
print()
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print()
print('-='*15)
opcao = int(input('Digite sua opção: '))
print('-='*15)
print()

if opcao == 1:
    print(f'O número {num} convertido para Binário é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para Octal é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para Hexadecimal é: {hex(num)[2:]}')
else:
    print('Algo deu errado.')
print('-='*15)
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome da cidade: ')).strip().upper().split()

if cidade[0] == 'SANTO':
    print('Cidade começa com "SANTO"')
else:
    print('Cidade não começa com "SANTO"')
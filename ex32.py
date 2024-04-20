# Faça um programa que leia um ano qualquer e mostra se ele é BISSEXTO.

from datetime import date

ano = int(input('Digite um ano qualquer. Caso queira analisar o ano atual, digite "0": '))

# Verificando o ano atual
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO.')
else:  
    print(f'O ano de {ano} não é BISSEXTO.')
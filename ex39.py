# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = abs(nasc - ano_atual)

if idade < 18:
    print(f'Ainda vai se alistar, falta(m) {abs(idade - 18)} ano(s).')
elif idade > 18:
    print(f'Já passou do tempo do alistamento, está {abs(idade - 18)} ano(s) atrasado.')
else:
    print(f'Está na hora de se alistar.')
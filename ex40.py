# Crie um programa que laia duas notas de um aluno e calcula sua média. mostrando uma mensagem no final, de acordo com a média atingida: 
# – Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media < 5:
    print('REPROVADO!')
elif 5 <= media < 7: # media >= 5 and media < 7
    print('RECUPERAÇÃO!')
elif media >= 7:
    print('APROVADO!')
else:
    print('Algo deu errado!')
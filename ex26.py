'''
Faça um programa que laia uma frase pelo teclado a mostra:
a) Quantas vezes aparece a letra "A".
b) Em que posição ela aparece a primeira vez.
c) Em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "a" aparece {frase.count("a")} vezes')
print(f'A letra "a" aparece pela primeira vez no índice {frase.find("a")}')
print(f'A letra "a" aparece pela última vez no índice {frase.rfind("a")}')
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

info = input('Digite algo: ')

print('O tipo desse valor é: ', type(info))
print('Contém apenas espaços?', info.isspace())
print('É um número?', info.isnumeric())
print('É alfabético?', info.isalpha())
print('É alfanumérico?', info.isalnum())
print('Está em maiúsculo?', info.isupper())
print('Está em minúsculo?', info.islower())
print('Está capitalizado?', info.istitle())
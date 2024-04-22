# Desenvolva uma lógica que leia o peso e a altura de uma pessoa. calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# · Abaixo da 18.5: Abaixo do Peso
# · Entre 18.5 e 25: Peso ideal
# · 25 até 30: Sobrepeso
# · 30 até 40: Obesidade
# · Acima de 40: Obesidade morbida

# IMC = peso / (altura * altura)

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25 :
    print('Peso ideal')
elif 25 <= imc < 30 :
    print('Sobrepeso')
elif 30 <= imc < 40 :
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')
else:
    print('Algo deu errado!')
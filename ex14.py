# Escreva um programa que converta uma temperatura digitada em °C e converta para F.
# (valor °C × 9/5) + 32 = valor °F

celsius = float(input('Digite a temperatura em °C: '))

fahrenheit = (celsius * 9/5) + 32

print(f'O valor de {celsius}°C em Fahrenheit é {fahrenheit}°F')
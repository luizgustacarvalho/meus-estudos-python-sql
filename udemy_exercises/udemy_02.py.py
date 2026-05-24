"""
Calculadora de IMC Interativa
"""

nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura (ex: 1.80): '))
peso = float(input('Digite seu peso (kg): '))

# Lógica do IMC
# Usei ** 2 porque é o mesmo da regra do IMC altura * altura
imc = peso / (altura ** 2)

# Resultados finais
print(f'\n--- Resultado ---')
print(f'{nome}, seu IMC é: {imc:.2f}')

# Certificando se encaixa com algumas das alternativas
if imc < 18.5:
    print('Classificação: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Classificação: Peso normal')
elif 25 <= imc < 30:
    print('Classificação: Sobrepeso')
else:
    print('Classificação: Obesidade')
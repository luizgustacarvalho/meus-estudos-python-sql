print("=== Análise de Empréstimo Bancário ===")
entrada_idade = input('Digite sua idade: ')
entrada_salario = input('Digite seu salário mensal: ')

try:
    idade = int(entrada_idade)
    salario = float(entrada_salario)
    idade_ok = 18 <= idade <= 65
    salario_ok = salario >= 2500

    if idade_ok and salario_ok:
        print('\n✅ STATUS: Empréstimo Pré-Aprovado!')
    else:
        print('\n❌ STATUS: Empréstimo Negado.')
        if not idade_ok:
            print(f'- Motivo: A idade deve ser entre 18 e 65 (Atual: {age}).')
        if not salario_ok:
            print(f'- Motivo: Salário mínimo é R$ 2.500,00 (Atual: R$ {salario:.2f}).')
except ValueError:
    print('\n⚠️ ERRO: Digite números válidos para idade e salário.')
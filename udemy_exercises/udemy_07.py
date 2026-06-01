
import copy

produtos = [
    {'nome': 'Macarrão', 'preco': 10.00},
    {'nome': 'Feijão', 'preco': 22.32},
    {'nome': 'Arroz', 'preco': 10.11},
    {'nome': 'Macaxeira', 'preco': 105.87},
    {'nome': 'Batata Doce', 'preco': 69.90},
]

preco = []
novo_preco = 1.1

while True:
    venda = input("""
Informe qual produto deseja:
1- Macarrão (Digite 0)
2- Feijão (Digite 1)
3- Arroz (Digite 2)
4- Macaxeira (Digite 3)
5- Batata Doce (Digite 4) >> """)

    try:
        venda = int(venda)
        if venda < 0 or venda > 4:
            print(f'ERRO: O número {venda} não corresponde a nenhum produto cadastrado.')

            continuar = input('Deseja tentar novamente? [S/N]: ').strip().upper()
            if continuar == 'S':
                continue
            else:
                print('Encerrando o programa de vendas.')
                break  
        if venda == 0:
            preco_atual = produtos[0]['preco']
            preco_com_aumento = preco_atual * novo_preco
            print(f'O valor do produto é: R$ {preco_atual:.2f}')
            print(f'O novo valor com 10% é: R$ {preco_com_aumento:.2f}')

        elif venda == 1:
            preco_atual = produtos[1]['preco']
            preco_com_aumento = preco_atual * novo_preco
            print(f'O valor do produto é: R$ {preco_atual:.2f}')
            print(f'O novo valor com 10% é: R$ {preco_com_aumento:.2f}')

        elif venda == 2:
            preco_atual = produtos[2]['preco']
            preco_com_aumento = preco_atual * novo_preco
            print(f'O valor do produto é: R$ {preco_atual:.2f}')
            print(f'O novo valor com 10% é: R$ {preco_com_aumento:.2f}')

        elif venda == 3:
            preco_atual = produtos[3]['preco']
            preco_com_aumento = preco_atual * novo_preco
            print(f'O valor do produto é: R$ {preco_atual:.2f}')
            print(f'O novo valor com 10% é: R$ {preco_com_aumento:.2f}')

        elif venda == 4:
            preco_atual = produtos[4]['preco']
            preco_com_aumento = preco_atual * novo_preco
            print(f'O valor do produto é: R$ {preco_atual:.2f}')
            print(f'O novo valor com 10% é: R$ {preco_com_aumento:.2f}')
        break

    except ValueError:
        print('ERRO: Você digitou letras ou caracteres inválidos. Por favor, digite somente números inteiros.')

        continuar = input('Deseja tentar novamente? [S/N]: ').strip().upper()
        if continuar == 'S':
            continue
        else:
            print('Encerrando o programa de vendas.')
            break

novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] *= novo_preco
    produto['preco'] = round(produto['preco'], 2)

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome = sorted(
    produtos_ordenados_por_nome,
    key=lambda item: item['nome'],
    reverse=True
)

produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco = sorted(
    produtos_ordenados_por_preco,
    key=lambda item: item['preco']
)

# Exibição das listas do desafio
print('\n' + '=' * 50)
print('DADOS PROCESSADOS DO DESAFIO:')
print('=' * 50)

print('1. PRODUTOS ORIGINAIS (Intactos):')
print(*produtos, sep='\n')
print('-' * 50)

print('2. NOVOS PRODUTOS (Preço + 10%):')
print(*novos_produtos, sep='\n')
print('-' * 50)

print('3. PRODUTOS ORDENADOS POR NOME (Z-A):')
print(*produtos_ordenados_por_nome, sep='\n')
print('-' * 50)

print('4. PRODUTOS ORDENADOS POR PREÇO (Menor para Maior):')
print(*produtos_ordenados_por_preco, sep='\n')
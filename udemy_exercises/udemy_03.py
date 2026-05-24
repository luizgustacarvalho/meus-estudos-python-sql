nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Nome: {nome} | Idade: {idade}')
    if int(idade) >= 18: print('Maior de idade.')
    else: print('Menor de idade.')

    if ' ' in nome: print('Contém espaços.')
    else: print('Não contém espaços.')

    print(f'Invertido: {nome[::-1]}')
    print(f'Total letras: {len(nome)}')
    print(f'Primeira: {nome[0]} | Última: {nome[-1]}')
else:
    print('❌ Erro: Campos vazios.')
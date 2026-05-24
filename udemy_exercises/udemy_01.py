"""
Script para processamento e exibição de dados cadastrais.
Calcula a maioridade com base na idade fornecida e exibe os dados formatados.
"""

# Definição das variáveis (Dados de entrada)
nome = 'Luiz'
sobrenome = 'Carvalho'
idade = 21
ano_de_nascimento = 2005
altura_em_metros = 1.98

# Lógica de negócio
maior_de_idade = idade >= 18

# Exibição dos dados formatados (Output)
print(f'Nome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Idade: {idade}')
print(f'Maior de idade: {"Sim" if maior_de_idade else "Não"}')
print(f'Ano de nascimento: {ano_de_nascimento}')
print(f'Altura em metros: {altura_em_metros:.2f}m')
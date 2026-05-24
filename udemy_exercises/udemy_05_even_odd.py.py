# --- Seção 1: Análise de Nome ---
nome = input('Digite seu nome: ').strip()
tamanho = len(nome.replace(' ', ''))
if tamanho > 0:
    print(f'Bem-vindo, {nome}!')
    if tamanho <= 4: print('Seu nome é curto.')
    elif 5 <= tamanho <= 6: print('Seu nome é normal.')
    else: print('Seu nome é muito grande.')
else: print('Erro: Nome vazio.')

# --- Seção 2: Paridade (Par/Ímpar) ---
num = input('Digite um número inteiro: ')
if num.isdigit():
    n = int(num)
    res = "par" if n % 2 == 0 else "ímpar"
    print(f'O número {n} é {res}.')

# --- Seção 3: Saudação ---
hora = input('Hora atual (0-23): ')
try:
    h = int(hora)
    if 0 <= h <= 11: print("Bom dia!")
    elif 12 <= h <= 17: print("Boa tarde!")
    elif 18 <= h <= 23: print("Boa noite!")
except: print("Erro na hora.")
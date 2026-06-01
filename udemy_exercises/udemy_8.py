def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

def executa(funcao, *args):
    def adiada(*proximos_args):
        return funcao(*args, *proximos_args)

    return adiada


soma_cinco = executa(soma, 5)
multiplica_por_dez = executa(multiplica, 10)

print(soma_cinco(10))
print(multiplica_por_dez(5))
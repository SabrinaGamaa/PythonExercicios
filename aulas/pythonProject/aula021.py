def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Sabrina Gama do Canal aqui na minha casa.
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')


help(contador)

print('-=' * 30)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(8, 4)
r3 = somar()
print(f'Meus cálculos deram {r1}, {r2}, {r3}.')

print('-=' * 30)

def teste1():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste1()
print(f'No program principal, x da erro por estar dentro def')

print('-=' * 30)

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'a dentro vale {a}')
    print(f'b dentro vale {b}')
    print(f'c dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


from random import randint

def numero(co, te):
    lista = list()
    print('Sorteado 5 valores da lista: ', end='')
    for valor in range(0, 5):
        sorteio = randint(co, te)
        lista.append(sorteio)

    for sor in lista:
        print(f'{sor}', end=' ')
    print('PRONTO!')


    print(f'Somando os valores PARES de {lista}, temos ', end='')
    pares = 0
    for par in lista:
        if par % 2 == 0:
            pares += par
    print(pares)



c = int(input('Começar: '))
t = int(input('Terminar: '))
numero(c, t)

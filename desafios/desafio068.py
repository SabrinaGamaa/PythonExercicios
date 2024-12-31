from random import randint
cont = 0
while True:
    n1 = int(input('Digite um número: '))
    n2 = ' '
    sorteio = randint(0, 10)
    soma = n1 + sorteio

    while n2 not in 'PI':
        n2 = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]

    print(f'Você jogou {n1} e o computador {sorteio}. Total de {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')

    if n2 == 'P':
        if soma % 2 == 0:
            print('Você ganhou!!')
            cont += 1
        else:
            break
    elif n2 == 'I':
        if soma % 2 == 1:
            print('Você ganhou!!')
            cont += 1
        else:
            break
    print('Vamos jogar novamente...')
print('Você perdeu!')
print(f'GAMER OVER!!!! Você venceu {cont} vezes')

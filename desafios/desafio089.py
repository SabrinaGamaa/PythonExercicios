lista = []
nota = 0
n1 = n2 = 0
while True:
    nome = str(input('Nome: '))

    while True:
        n1 = float(input('Nota 1: '))
        while n1 > 10 or n1 <= -1:
            print('\033[31mValor invalido... (0, 10)\033[m')
            n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))

        while n2 > 10 or n2 <= -1:
            print('\033[31mValor invalido... (0, 10)\033[m')
            n2 = float(input('Nota 2: '))
        else:
            break

    soma = (n1 + n2) / 2
    lista.append([nome, [n1, n2], soma])
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'{"Nª.":<6}{"Nome":<10}{"MÉDIA:":>8}')
print('--' * 30)
for i, a in enumerate(lista):
    print(f'{i:<6}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 30)
    nota = int(input('Mostrar nota de qual aluno? (999 interrompe):'))
    if nota == 999:
        break
    if nota > len(lista) - 1:
        print(f'\033[31mDigite um valor válido. De 0 a {len(lista) - 1}\033[m')
    if nota <= len(lista) - 1:
        print(f'A nota do aluno(a) {lista[nota][0].upper()} foram {lista[nota][1]} e sua média foi de {lista[nota][2]}')
print('-=' * 3, ' PROGRAMA ENCERRRADO! ', '-=' * 3)


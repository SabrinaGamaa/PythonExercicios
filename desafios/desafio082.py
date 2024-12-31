lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    sair = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while sair not in 'NS':
        sair = str(input('Tente novamente...Deseja continuar? [S/N] ')).upper().strip()[0]
    if sair in 'N':
        break
print('-=' * 30)
print(f'Os elementos digitados foram {par + impar}')
print(f'Elementos PARES: {par}')
print(f'Elementos IMPARES: {impar}')

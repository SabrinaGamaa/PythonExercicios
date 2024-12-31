galera = []
dado = []
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: kg')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        elif dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    sair = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while sair not in 'SN':
        sair = str(input('Tenta novamente...Quer continuar? [S/N] ')).upper().strip()[0]
    if sair in 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O maior peso foi de {mai}kg.:', end=' ')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {men}kg.:', end=' ')
for p in galera:
    if p[1] == men:
        print(f'{p[0]}', end=' ')

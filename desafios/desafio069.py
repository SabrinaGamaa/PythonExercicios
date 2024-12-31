dezoito = homens = mulheres = 0
while True:
    print('-=' * 20)
    idade = int(input('Digite a idade: '))

    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual seu sexo: [M/F] ')).upper().strip()[0]

    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar cadastrando? [S/N] ')).strip()[0].upper()
    if sair == 'N':
        break

    if idade >= 18:
        dezoito += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade <= 20:
        mulheres += 1

print('\033[31m==-\033[m' * 20)
print(f'Tem \033[32m{dezoito}\033[m pessoas maiores de 18 anos.')
print(f'Foram cadastrados \033[32m{homens}\033[m HOMENS')
print(f'Tem \033[32m{mulheres}\033[m mulheres com menos de 20 anos.')


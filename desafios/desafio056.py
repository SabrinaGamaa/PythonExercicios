midade = 0
maioridade = 0
nomemaior = 0
mulheres = 0
for pessoas in range(1, 5):
    print('{}{}ª PESSOA.{}'.format('-=' * 25, pessoas, '-=' * 25))
    nome = str(input('Qual é o seu nome completo? '))
    idade = int(input('Quantos anos você tem? '))
    sexo = int(input('[ 1 ] para Homem\n[ 2 ] para Mulher\nDigite aqui: '))
    #A média de idade no grupo é {:.0f} anos
    if idade > 1:
        midade += idade / 4

    #O nome do homem mais velho tem {} e o nome
    if sexo == 1 and pessoas == 1:
        maioridade = idade
        nomemaior = nome
    else:
        if sexo == 1 and idade > maioridade:
            maioridade = idade
            nomemaior = nome

    #Têm {:.0f} mulheres com menos de 20 anos
    if sexo == 2 and idade <= 20:
        mulheres += 1

print('\033[34m-=\033[m' * 25)
print('A média de idade no grupo é {:.0f} anos'.format(midade))
print('O nome do homem mais velho tem {} e o nome {}'.format(maioridade, nomemaior))
print('Têm {:.0f} mulheres com menos de 20 anos'.format(mulheres))

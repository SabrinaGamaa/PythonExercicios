'''Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se quer ou não continuar'''
cont = 0
num = 'S'
soma = 0
media = 0
maior = 0
menor = 0
while num == 'S':
    n1 = int(input('Digite um número: '))
    cont += 1
    soma += n1
    media = soma / cont
    if num == 'S':
        num = str(input('Deseja Continuar? [N/S]  ')).upper()
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
print('Você digitou {} e a média desses número é de {:.1f}'.format(cont, media))
print('O menor número foi {} e o maior {}'.format(menor, maior))
print('FIM')

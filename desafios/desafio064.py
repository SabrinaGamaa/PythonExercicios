'''Crie um programa que leia varios números inteiros pelo teclado. O progama só vai parar quando o usuário
digitar o valor de 999, que é a condição de parada.No final, mostre quantos números foram digitados e qual foi
a soma entre eles.( desconsiderando o 999 )'''
cont = soma = 0
n1 = int(input('Digite um número [999 para parar]: '))
while n1 != 999:
    cont += 1
    soma += n1
    n1 = int(input('Digite um número: '))
print('Você digitou {} números e a soma entre eles é de {}'.format(cont, soma))
print('FIM')

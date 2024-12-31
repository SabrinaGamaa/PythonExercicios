n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
if n1 > n2:
    print('O primeiro valor {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor {} é maior que {}'.format(n2, n1))
elif n1 == n2:
    print('O primeiro {} e o segundo {} valor, são iguais'.format(n1, n2))
print('Obrigado por ter participado da brincadeira!')

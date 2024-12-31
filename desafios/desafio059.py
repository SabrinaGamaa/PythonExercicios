from time import sleep
sair = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while sair != 5:
    print('-==' * 25)
    sleep(2)
    print('''VOCÊ ENTROU NO PROGRAMA GAMA´S
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    num = int(input('>>>>> Digite sua escolha: '))
    if num == 5:
        sair = 5
    elif num == 1:
        somar = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, somar))
    elif num == 2:
        multi = n1 * n2
        print('A multiplicação de {} * {} = {}'.format(n1, n2, multi))
    elif num == 3:
        if n1 > n2:
            print('Os números {} e {} o MAIOR VALOR É {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('Os números {} e {} o MAIOR VALOR É {}'.format(n1, n2, n2))
    elif num == 4:
        print('Informe os novos números.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Valor inválido. Tente novamente')
print('Muito obrigado pelo prefêrencia!!')

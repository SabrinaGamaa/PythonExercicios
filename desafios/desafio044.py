print('{:=^40}'.format(' LOJAS GAMA´S '))
valor = float(input('Digite o valor do item R$ '))
print('\033[35m=-=' * 25)
print('''Escolha a forma de pagamento:
[ 1 ] = Á VISTA/CHEQUE
[ 2 ] = Á VISTA NO CARTÃO
[ 3 ] = 2x NO CATÃO
[ 4 ] = 3x ou MAIS NO CARTÃO''')
pagamento = int(input('Digite o número da forma de pagamento: '))
print('\033[35m=-=\033[m' * 25)
print('Seu item custa R${:.2f}'.format(valor))
if pagamento == 1:
    print('PARÁBENS, você recebeu um desconto de 10%, Seu item ficará R${:.2f}'.format(valor - (valor * 10 / 100)))
elif pagamento == 2:
    print('PARÁBENS, você ganhou um desconto de 5%, seu item ficará R${:.2f}'.format(valor - (valor * 5 / 100)))
elif pagamento == 3:
    print('Obrigado por sua escolha!')
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f}, você recebe um juros de 20%, total com o valor do produto ficará R${:.2f}'.format(parcelas,((valor * 20 / 100) + valor) / parcelas, valor + (valor * 20 / 100)))
    termos = int(input('Você concorda com esses termos? \n[ 1 ] para SIM.\n[ 2 ] para NÃO.\nDigite aqui: '))
    if termos == 1:
        print('Você concordou com os termos de compra. Obrigado por sua compra!')
    elif termos == 2:
        print('Você NÃO concordou com os termos de compra sua compra será cancelada, lamentamos pelo transtorno.')

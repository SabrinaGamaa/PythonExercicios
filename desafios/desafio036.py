casa = float(input('\033[1;31mQual o valor da casa desejada? '))
salario = float(input('Qual sua renda mensal? '))
anos = int(input('Em quantas anos você gostaria de pagar? \033[m'))
parcelas = anos * 12
prestacao = casa / parcelas
trinta = (salario * 30) / 100
if prestacao < trinta:
    print('\033[1;32mPARÁBENS VOCÊ FOI APROVADO!!!\033[m\nSuas parcelas ficaram R${:.2f} em {:.0f}x'.format(prestacao, parcelas))
else:
    print('Infelizmente não foi possível aprovar seu limite.\nAs parcelas ficaria R${:.2f}\n'
          'Por favor tente novamente daqui uns meses.'.format(prestacao, trinta))
print('\033[1;34mObrigado por entrar em contato.\033[m')


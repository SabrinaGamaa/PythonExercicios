from datetime import date
print('A confederação Nacional de natação precisa saber seu ano de nascimento, para saber sua categoria')
n1 = int(input('Digite o ano que você nasceu: '))
idade = - (n1 - date.today().year)
if idade <= 9:
    print('Você está com {} anos, sua categoria é \033[1;36mMIRRIM\033[m'.format(idade))
elif idade <= 14:
    print('Voce está com {} anos, seua categoria é \033[1;35mINFANTIL\033[m'.format(idade))
elif idade <= 19:
    print('Você está com {} anos, sua categoria é \033[1;34mJUNIOR\033[m'.format(idade))
elif idade == 20:
    print('Você está com 20 anos, sua categoria é \033[1;33mSÊNIOR\033[m')
else:
    print('Você está com {} anos, sua categoria é \033[1;32mMASTER\033[m'.format(idade))

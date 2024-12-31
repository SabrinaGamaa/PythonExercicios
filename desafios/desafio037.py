from time import sleep
n1 = int(input('\033[33mEscreva um número inteiro: \033[m'))
print('''
DIGITE [ 1 ] para BINARIO
DIGITE [ 2 ] para OCTAL
DIGITE [ 3 ] para HEXADECIMAL''')
opcao = int(input('Digite seu escolha: \033[m'))
print('ANALISANDO...')
sleep(2)
if opcao == 1:
    print('O seu número inteiro é {} e o BINARIO é {}'.format(n1, bin(n1)[2:]))
elif opcao == 2:
    print('O seu número inteiro é {} e o OCTAL é {}'.format(n1, oct(n1)[2:]))
elif opcao == 3:
    print('O seu número inteiro é {} e seu HEXADECIMAL é {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção invalida.')

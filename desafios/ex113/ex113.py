def leiaint(msg=0):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor! Digite um número inteiro válido.')
            continue
        except Exception as erro:
            print(f'O erro de num é {erro.__class__}')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar os dados!')
            n = 0
            return n
        else:
            return n


def leiareal(msg=0):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Por favor! Digite um número inteiro válido.')
            continue
        except Exception as erro:
            print(f'Erro de real é {erro.__class__}')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar os dados!')
            n = 0
            return n
        else:
            return n


num = leiaint('Digite um número Inteiro: ')
dois = leiareal('Digite um número Real: ')

print(f'O valor inteiro é {num} e o Real é {dois}')


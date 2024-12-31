def cabecalho(msg):
    print('-' * 40)
    print(f'{msg}'.center(40))
    print('-' * 40)


def linha(tam=40):
    return '-' * tam


def leiadados(msg):
    try:
        cabecalho('MENU DO SISTEMA')
        for i, c in enumerate(msg):
            print(f'\033[33m{i+1}\033[m - \033[34m{c}\033[m')
        print(linha())
        n = int(input(f'\033[33m{'Sua Opção: '}\033[m'))
    except (ValueError, TypeError):
        print(f'\033[31mERRO! Digite um número inteiro.\033[m')
    except KeyboardInterrupt:
        print('\033[31mUsuario preferiu não informar.\033[m')
    else:
        return n

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




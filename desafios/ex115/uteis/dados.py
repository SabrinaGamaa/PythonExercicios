def cabecalho(msg):
    print('-' * 40)
    print(f'{msg}'.center(40))
    print('-' * 40)


def linha(tam=40):
    return '-' * tam


def leiadados(msg):
    pessoas = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']
    while True:
        cabecalho('MENU DO SISTEMA')
        for i, c in enumerate(pessoas):
            print(f'\033[33m{i+1}\033[m - \033[34m{c}\033[m')
        print(linha())
        try:
            n = int(input(f'\033[33m{msg}\033[m'))
            if not n <= len(pessoas):
                print('\033[31mDigite um valor valido!\033[m')
                continue
            elif n == 1:
                cabecalho('Opção 1!')
                continue
            elif n == 2:
                cabecalho('Opção 2!')
                continue
            elif n == 3:
                cabecalho('Saindo do sistema... Até logo!')
                break
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro.\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuario preferiu não informar.\033[m')
            break
        else:
            break
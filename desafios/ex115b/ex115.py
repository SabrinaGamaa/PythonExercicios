from pythonProject1.desafios.ex115b.lib.arquivo import *
from pythonProject1.desafios.ex115b.lib.interface import *


arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    pessoas = leiadados(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if pessoas == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    elif pessoas == 1:
        cabecalho(f'{'PESSOAS CADASTRADAS'}')
        leiaarquivo(arq)
    elif pessoas == 2:
        cabecalho(f'{'NOVO CADASTRO'}')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastramento(arq, nome, idade)
    else:
        print('\033[31mDigite um valor valido!\033[m')




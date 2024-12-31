def arquivoexiste(nome):
    try:
        ar = open(nome, 'rt')
        ar.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True
def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso')

def leiaarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastramento(arq, nome='Usuario', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'Erro! Na tentativa de cadastramento.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao salvar os dados, Por favor tente novamente.')
        else:
            print(f'Novo registro de {nome} adicionado!')

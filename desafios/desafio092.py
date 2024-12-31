from datetime import  datetime
ano = datetime.today().year
dados = dict()

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = ano - nascimento
cart = int(input('Carteira de Trabalho (0 não tem): '))
dados['ctps'] = cart
while True:
    if cart == 0:
        break
    anocont = int(input('Ano de Contratação: '))
    dados['contratação'] = anocont
    salario = float(input('Salário: R$'))
    dados['salário'] = salario
    dados['aposentadoria'] = dados["idade"] + ((anocont + 35) - ano)
    break
print('-=' * 30)
for k, e in dados.items():
    print(f'    - {k} tem o valor de {e}')
print(dados)


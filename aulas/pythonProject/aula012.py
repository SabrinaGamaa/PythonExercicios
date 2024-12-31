nome = str(input('Digite seu nome: ')).strip()
if 'sabrina' in nome:
    print('Seu nome é muito lindo!')
elif nome == 'Rose' or nome == 'Silva':
    print('Nossa que sobrenome lindo!')
else:
    print('Seu nome é tão comum.')
print('Tenha um bom dia, {}!'.format(nome))

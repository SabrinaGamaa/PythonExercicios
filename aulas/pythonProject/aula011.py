print('\033[0;33;44mOlá, mundo!')
print('\033[7mOlá, mundo!')
print('\033[0;30;41mOlá, mundo!')
print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[4;30;45mOlá, mundo!\033[m')
a = 5
b = 3
print('Os valores são \033[1;30;41m{}\033[m e \033[33m{}\033[m'.format(a, b))
nome = 'Sabrina'
cores = {'limpa': '\033[m',
        'amarelo': '\033[33m'}
print('Muito prazer em te conhecer {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))

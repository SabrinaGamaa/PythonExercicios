palavras = ('Aprender',
            'Programar',
            'Linguagem',
            'Python',
            'Curso',
            'Gratis',
            'Estudar',
            'Praticar',
            'Trabalhar',
            'Mercador',
            'Programador',
            'Futuro'
            )
cont = 0
for c in palavras:
    print(f'\nNa palavra \033[32m{c.upper()}\033[m temos: ', end='')
    for letras in c:
        if letras.lower() in 'aeiou':
            cont += 1
            print(f'\033[31m{letras}\033[m', end=' ')
print(f'\nTotal de {cont} vogais')

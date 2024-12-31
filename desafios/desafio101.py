def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos: ', end='')
        return 'NÃO VOTA.'
    elif 16 <= idade <= 18:
        print(f'Com {idade} anos: ', end='')
        return 'VOTO OPCIONAL.'
    elif 18 <= idade <= 65:
        print(f'Com {idade} anos: ', end='')
        return 'VOTO OBRIGATORIO.'
    else:
        print(f'Com {idade} anos: ', end='')
        return 'VOTO OPCIONAL.'


nasceu = int(input('Em que ano você nasceu? '))
print(voto(nasceu))

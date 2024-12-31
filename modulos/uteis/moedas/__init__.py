def metade(m=0):
    res = m / 2
    return f'{res:.2f}'


def doblo(m=0):
    return m * 2


def aumentar(m=0, taxa=0):
    return (m * taxa / 100) + m


def diminuir(m=0, taxa=0):
    return m - (m * taxa / 100)


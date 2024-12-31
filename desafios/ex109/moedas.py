def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moedas(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moedas(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moedas(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moedas(res)


def moedas(preco = 0, moedas = 'R$'):
    return f'{moedas}{preco:>.2f}'.replace('.', ',')
